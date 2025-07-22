import os.path
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm
from utils import *
from SQLServer import SQLServerManager

sql_manager = SQLServerManager()
database = sql_manager.database

column_mapper = "column_mapping.csv"
DIR_DOWNLOADS = 'Downloads'
DIR_CHUNKS = 'chunk_files'
DIR_ERRORS = 'Errors'
linhas_por_chunk = 1000000


def download_data(url, retries=3):

    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)



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

    drop_directory(DIR_DOWNLOADS)
    return None


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
        sql_manager.recreate_sql_table(df, table_name)
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
        sql_manager.recreate_sql_table(df_all_chunks, table_name)

        # returns list with all chunks
        return chunk_files



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


def download_datasets(dataset_name, url):

    try:
        create_directory(DIR_DOWNLOADS)
        drop_directory(DIR_ERRORS)
        create_directory(DIR_ERRORS)

        print('\n---------')
        print(dataset_name.upper())

        # download file (last modified)
        file_path = download_data(url)
        table_name = (os.path
                      .basename(file_path)
                      .removesuffix('.tsv'))

        # Deletes old downloads (only most recent file is kept)
        delete_old_downloads(dataset_name)

        # Creates table & gets the files to Bulk insert
        create_directory(DIR_CHUNKS)

        files = prepare_to_insert_sql(
            file_path,
            table_name
        )

        for file in files:
            sql_manager.bulk_insert_csv(
                os.path.abspath(file),
                table_name,
                os.path.abspath(DIR_ERRORS),
                field_terminator="\t")

    except Exception as e:
        print(e)
    finally:
        drop_directory(DIR_CHUNKS)








