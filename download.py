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
connection = engine.connect()


def download_data(url, retries=3):
    """
    Fetches data from a URL with retry mechanism in case of ReadTimeout error,
    and displays a progress bar while downloading.
    """
    filename = url.split('/')[-1]

    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    print(f"Downloading {filename}...")
    filepath = os.path.join(DIR_DOWNLOADS, filename.replace('.txt', '.tsv'))


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
                print(f"{filepath.split('\\')[1]} already exists, skipping.")
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


def create_sql_table(df: pd.DataFrame, table_name: str):
    table_name = table_name.replace(".tsv", "").replace(".csv", "")
    connection.execute(text(f"IF OBJECT_ID('[{table_name}]', 'U') IS NOT NULL DROP TABLE [{table_name}]"))
    create_sql = generate_create_table(df, table_name)
    # print("Criando tabela com SQL:\n", create_sql)
    print("Criando tabela com SQL:\n", table_name)
    connection.execute(text(create_sql))
    connection.commit()



def prepare_to_insert_sql(file_path, table_name):
    # file_name = os.path.basename(file_path)
    # table_name = file_name.split('.')[0]

    row_count = count_file_rows(file_path)
    print(f"{row_count:,} total rows.")

    chunk_files = []

    sample_from_chunks = pd.DataFrame()
    reader = pd.read_csv(file_path, encoding='utf-8', sep="\t", low_memory=False, chunksize=linhas_por_chunk)
    for i, chunk in enumerate(reader):

        # Translate columns to english / maps columns & Convert column dtypes
        df = map_columns(chunk, mapping_file=column_mapper)
        df = df.convert_dtypes()

        # Create a chunk from file
        chunk_path = os.path.join(DIR_CHUNKS, f"chunk_{table_name}_part{i + 1}.tsv")
        df.to_csv(chunk_path, sep="\t", index=False, encoding='utf-8')
        chunk_files.append(os.path.basename(chunk_path))
        sample_from_chunks = pd.concat(
            [sample_from_chunks, df.sample(frac=0.1)]
        )

    print("Created chunk files")
    # Creates the table from a sample of the chunks
    create_sql_table(sample_from_chunks, table_name)
    return chunk_files


def bulk_insert_file_to_sql(file, table_name):
    errors_dir = os.path.join(os.getcwd(), DIR_ERRORS)
    chunks_dir = os.path.join(os.getcwd(), DIR_CHUNKS)

    file_abs_path = os.path.abspath(os.path.join(chunks_dir, file))
    sep = "\t"
    try:
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
        # print(sql)
        print(f"A importar: {file} to {table_name} SQL table")

        # input("PRESS TO IMPORT")
        connection.execute(text(sql))
        connection.commit()

    except Exception as e:
        print(f"Erro ao importar {file}: {e}")
        linhas_com_erro = []


        for match in re.finditer(r"row (\d+), column", str(e)):
            linhas_com_erro.append(int(match.group(1)))
        if linhas_com_erro:
            print(f"Linhas com erro detectadas: {linhas_com_erro}")
            erro_csv = os.path.join(errors_dir, f"errors_{file}")

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



def download_datasets(datasets):

    drop_directory(DIR_ERRORS)
    create_directory(DIR_ERRORS)

    create_directory(DIR_DOWNLOADS)
    create_directory(DIR_CHUNKS)

    try:
        for dataset_name, url in datasets.items():

            file_path = download_data(url)
            table_name = os.path.basename(file_path).split('.')[0]

            # Splits file into chunks & Creates table
            chunk_files = prepare_to_insert_sql(file_path, table_name)

            for chunk_file in chunk_files:
                bulk_insert_file_to_sql(chunk_file, table_name)

    except Exception as e:
        print(e)
    finally:
        connection.close()
        drop_directory(DIR_CHUNKS)








