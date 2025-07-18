import os
import time
import shutil
import pandas as pd
from dotenv import load_dotenv


def get_connection_string(engine):
    load_dotenv("config.env")

    database = os.getenv('DB_NAME')
    server = os.getenv('DB_SERVER')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASS')
    driver = "ODBC+Driver+17+for+SQL+Server"

    connection_string = None

    if engine == "sqlalchemy":
        if server == 'localhost':
            # Windows Auth on localhost
            connection_string = (
                f"mssql+pyodbc://@{server}/{database}"
                f"?driver={driver}&trusted_connection=yes"
            )
        else:
            # SQL Auth on remote
            connection_string = (
                f"mssql+pyodbc://{username}:{password}@{server}/{database}"
                f"?driver={driver}"
            )


    if engine == 'pyodbc':
        if server == 'localhost':
            # Windows Auth on localhost
            connection_string = (
                "DRIVER={ODBC Driver 17 for SQL Server};"
                f"SERVER={server};"
                f"DATABASE={database};"
                "Trusted_Connection=yes;"
            )
        else:
            # SQL Auth on remote
            connection_string = (
                # "Driver={SQL Server};"
                "Driver={ODBC Driver 17 for SQL Server};"
                f"Server={server};"
                f"Database={database};"
                f"UID={username};"
                f"PWD={password};"
            )

    if not connection_string:
        raise Exception("Wrong engine/sql-connector provided")

    return connection_string



def infer_sql_type_from_dtype(serie: pd.Series) -> str:

    pandas_to_sql = {
        'int8': 'INT',
        'int16': 'INT',
        'int32': 'INT',
        'int64': 'INT',
        'float32': 'DECIMAL(18,4)',
        'float64': 'DECIMAL(18,4)'
    }
    dtype = str(serie.dtype).lower()
    max_len = serie.astype(str).str.len().max()

    return pandas_to_sql.get(dtype, f'VARCHAR({max_len})')


def generate_create_table(df: pd.DataFrame, nome_tabela):
    sql_cols = []
    for col in df.columns:
        tipo = infer_sql_type_from_dtype(df[col])
        sql_cols.append(f"[{col}] {tipo}")
    columns_sql_str = ",\n    ".join(sql_cols)
    return f"CREATE TABLE {nome_tabela} (\n {columns_sql_str} \n);"


def create_directory(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def drop_directory(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)


def count_file_rows(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

def time_it_took(start_time: float, action: str):
    end = time.time()
    print(f"{action} durou {end - start_time:.2f} segundos")

def get_column_mapping(mapping_file):
    return pd.read_csv(mapping_file)

def map_columns(df, mapping_file):
    csv_mapping = get_column_mapping(mapping_file)

    column_mapping = dict(zip(csv_mapping['original_name'], csv_mapping['new_name']))
    not_mapped_cols =  set(df.columns) - set(column_mapping.keys())
    if not_mapped_cols:
        print('Update column_mapping.csv')
        raise ValueError(f"Mapping of columns: {not_mapped_cols}")

    return df.rename(columns=column_mapping)


