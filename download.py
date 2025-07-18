import csv
import os.path
import re
from datetime import datetime
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
from utils import *
from sqlalchemy import create_engine, text


column_mapper = "column_mapping.csv"
DIR_DOWNLOADS = 'Downloads'
DIR_CHUNKS = 'CHUNKS'
DIR_ERRORS = 'Errors'
linhas_por_chunk = 1000000

connection_string = get_connection_string('sqlalchemy')
engine = create_engine(connection_string,
    fast_executemany=True)
database_name = engine.url.database


def download_data(url, retries=3):
    """
    Fetches data from a URL with retry mechanism in case of ReadTimeout error
    """
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    create_directory(DIR_DOWNLOADS)
    filename = url.split('/')[-1]
    filepath = os.path.join(DIR_DOWNLOADS, filename.replace('.txt', '.tsv'))
    print(f"\nDownloading {filename}...")

    try:
        with session.get(url, stream=True, timeout=(30, 120)) as r:
            r.raise_for_status()

            # add data ultima modificação ao nome do ficheiro
            response_last_modified_dt = datetime.strptime(r.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
            last_modified = str(response_last_modified_dt.strftime('%Y_%m_%d'))
            filepath = filepath.split('.tsv')[0] + f"_{last_modified}" + '.tsv'


            # Gets the FILE - SIZE IN BYTES from the response headers
            file_size_in_bytes = int(r.headers.get('Content-Length', 0))
            print(f"File size: {str(round(file_size_in_bytes/1024**3,2))} GB")

            if os.path.exists(filepath) and file_size_in_bytes == os.path.getsize(filepath):
                print(f"\n{filepath.split('\\')[1]} already exists, skipping.")
                return filepath


            chunk_size = 64 * 1024  # 64 KB
            with open(filepath, 'wb') as f, tqdm(
                total=file_size_in_bytes,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
                desc=filename,
                leave=True
            ) as bar:
                for chunk in r.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))

        print("Download completed successfully.")
        return filepath

    except requests.exceptions.ReadTimeout:
        print("ReadTimeout error: Server did not respond within the specified timeout.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return None


def recreate_sql_table(df: pd.DataFrame, table_name: str):

    table_name = table_name.replace(".tsv", "").replace(".csv", "")
    connection = engine.connect()

    try:
        # APAGAR TABELA SE EXISTE
        drop_table_stmt = text(f"IF OBJECT_ID('[{table_name}]', 'U') IS NOT NULL DROP TABLE [{table_name}]")
        connection.execute(drop_table_stmt)
        connection.commit()
        print('Apagou tabela: ', table_name)

        # CRIAR TABELA
        create_sql_stmt = text(generate_create_table(df, table_name))
        connection.execute(create_sql_stmt)
        connection.commit()
        print('Criou tabela SQL: ',table_name)

    except Exception as e:
        print(e)
    finally:
        connection.close()


def prepare_to_insert_sql(file_path, table_name):

    print("\nPreparar Bulk insert")

    row_count = count_file_rows(file_path)
    print(f"{row_count:,} total rows.")

    if row_count < linhas_por_chunk:
        df = pd.read_csv(file_path, encoding='utf-8', sep="\t", low_memory=False)
        df = map_columns(df, mapping_file=column_mapper)
        df = df.convert_dtypes()

        output_file = os.path.join(DIR_CHUNKS, table_name)
        df.to_csv(output_file, sep="\t", index=False, encoding='utf-8')
        recreate_sql_table(df, table_name)
        return [output_file]

    # Ficheiro tem mais que o limite maximo de rows
    else:
        chunk_files = []
        df_all_chunks = pd.DataFrame()
        create_directory(DIR_CHUNKS)
        print(f'Dividir em ficheiros de {linhas_por_chunk:,} rows.')


        reader = pd.read_csv(file_path, encoding='utf-8', sep="\t", low_memory=False, chunksize=linhas_por_chunk)
        for i, chunk in enumerate(reader):

            # Translate columns to english / maps columns & Convert column dtypes
            df = map_columns(chunk, mapping_file=column_mapper)
            df = df.convert_dtypes()

            # Creates a file
            chunk_path = os.path.join(DIR_CHUNKS, f"chunk_{table_name}_part{i + 1}.tsv")
            df.to_csv(chunk_path, sep="\t", index=False, encoding='utf-8')
            print(f"Criou ficheiro {chunk_path}")

            df_all_chunks = pd.concat([df_all_chunks, df])

            # Append to the chunk list
            chunk_files.append(chunk_path)

        # Creates the SQL TABLE from the sample
        recreate_sql_table(df_all_chunks, table_name)

        # returns list with all chunks
        return chunk_files


def bulk_insert_file_to_sql(file_path, table_name):

    drop_directory(DIR_ERRORS)
    create_directory(DIR_ERRORS)
    errors_dir = os.path.join(os.getcwd(), DIR_ERRORS)

    file_abs_path = os.path.abspath(file_path)
    file_basename = os.path.basename(file_path)
    connection = engine.connect()
    try:

        sep = "\t" # field terminator for TSV
        sql = f"""
            BULK INSERT {database_name}.dbo.[{table_name}]
            FROM '{file_abs_path}' 
            WITH (
                FIELDTERMINATOR = '{sep}',
                ROWTERMINATOR = '0x0D0A',
                FIRSTROW = 2,
                CODEPAGE = '65001',
                MAXERRORS = 10000
        )
        """

        print(f"A importar: {file_basename} to {table_name} SQL table")

        connection.execute(text(sql))
        connection.commit()

    except Exception as e:
        print(f"Erro ao importar {file_basename}: {e}")
        linhas_com_erro = []


        for match in re.finditer(r"row (\d+), column", str(e)):
            linhas_com_erro.append(int(match.group(1)))
        if linhas_com_erro:
            print(f"Linhas com erro detectadas: {linhas_com_erro}")
            erro_csv = os.path.join(errors_dir, f"errors_{file_basename}")

            with (open(file_abs_path, encoding="utf-8") as infile,
                  open(erro_csv, "w", newline="", encoding="utf-8") as outfile):
                reader = csv.reader(infile, delimiter="|")
                writer = csv.writer(outfile, delimiter="|")
                header = next(reader)
                writer.writerow(header)
                for i, row in enumerate(reader, start=2):
                    if i in linhas_com_erro:
                        writer.writerow(row)
            print(f"Linhas com erro guardadas em: {erro_csv}")

    finally:
        connection.close()




def delete_old_downloads(name):

    def extract_date(filename):
        match = re.search(r'(\d{4})_(\d{2})_(\d{2})', filename)
        if match:
            return datetime.strptime('_'.join(match.groups()), '%Y_%m_%d')
        return None

    files = [f for f in os.listdir(DIR_DOWNLOADS) if
             os.path.isfile(os.path.join(DIR_DOWNLOADS, f)) and f.lower().startswith(name.lower())]

    more_than_one_download_for_dataset =  len(files) > 1

    if more_than_one_download_for_dataset:
        files_with_dates = [(f, extract_date(f)) for f in files if extract_date(f) is not None]
        most_recent_file = max(files_with_dates, key=lambda x: x[1])[0]

        for fname, _ in files_with_dates:
            if fname != most_recent_file:
                file_path = os.path.join(DIR_DOWNLOADS, fname)
                os.remove(file_path)
                print(f"Deleted: {fname}")

        print(f"Kept: {most_recent_file}")



def download_datasets(datasets):

    try:
        for dataset_name, url in datasets.items():

            print('---------')
            #download file
            file_path_last_modified = download_data(url)

            table_name = os.path.basename(
                file_path_last_modified
            ).split('.')[0]

            # Creates table & gets the files to Bulk insert
            files = prepare_to_insert_sql(
                file_path_last_modified,
                table_name
            )

            for file in files:
                bulk_insert_file_to_sql(file, table_name)

            # Deletes old downloads (only most recent file is kept)
            delete_old_downloads(dataset_name)

    except Exception as e:
        print(e)
    finally:
        drop_directory(DIR_CHUNKS)








