from datetime import datetime
from tqdm import tqdm
import pyodbc
from dotenv import load_dotenv
import os
import pandas as pd
import re
import csv

load_dotenv("config.env")

class SQLServerManager:
    def __init__(self):
        self.server = os.getenv('DB_SERVER')
        self.database = os.getenv('DB_NAME')
        self.username = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASS')
        self.collation = os.getenv('DB_COLLATION')
        self.driver_name = "ODBC Driver 17 for SQL Server"

    def get_connection_string(self, engine='pyodbc', db_master=False):
        db = 'master' if db_master else self.database
        is_localhost = self.server.lower() == 'localhost'

        if engine == 'sqlalchemy':
            driver = self.driver_name.replace(" ", "+")
            if is_localhost:
                return f"mssql+pyodbc://@{self.server}/{db}?driver={driver}&trusted_connection=yes"
            return f"mssql+pyodbc://{self.username}:{self.password}@{self.server}/{db}?driver={driver}"

        elif engine == 'pyodbc':
            if is_localhost:
                return (
                    f"DRIVER={{{self.driver_name}}};"
                    f"SERVER={self.server};"
                    f"DATABASE={db};"
                    "Trusted_Connection=yes;"
                )
            return (
                f"DRIVER={{{self.driver_name}}};"
                f"SERVER={self.server};"
                f"DATABASE={db};"
                f"UID={self.username};"
                f"PWD={self.password};"
            )

        else:
            raise ValueError("Invalid engine. Choose 'sqlalchemy' or 'pyodbc'.")


    def _connect(self, db_master=False):
        return pyodbc.connect(self.get_connection_string("pyodbc", db_master), autocommit=True)


    def drop_database(self):
        # print(f"Dropping database: {self.database}")
        try:
            with self._connect(db_master=True).cursor() as cursor:
                cursor.execute(f"""
                    IF  EXISTS (SELECT name FROM sys.databases WHERE name = '{self.database}')
                    BEGIN
                    ALTER DATABASE [{self.database}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
                    DROP DATABASE IF EXISTS [{self.database}]
                    END
                """)
                print(f"✅ Dropped database: {self.database}")
        except Exception as e:
            print(f"❌ Error dropping database: {e}")


    def recreate_database(self):
        # print(f"Creating database: {self.database} with collation: {self.collation}")
        self.drop_database()
        try:
            with self._connect(db_master=True).cursor() as cursor:
                # Create database
                cursor.execute(f"""
                    IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = '{self.database}')
                    BEGIN
                        CREATE DATABASE [{self.database}] COLLATE {self.collation};
                    END
                """)
                print(f"✅ Created database '{self.database}'")

                # Set recovery model
                cursor.execute(f"""
                    ALTER DATABASE [{self.database}] SET RECOVERY SIMPLE;
                """)
        except Exception as e:
            print(f"❌ Error creating database: {e}")

    def get_sql_server_version(self):
        try:
            with self._connect(db_master=True).cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        SERVERPROPERTY('ProductVersion') AS Version,
                        SERVERPROPERTY('ProductLevel') AS Level,
                        SERVERPROPERTY('Edition') AS Edition
                """)
                row = cursor.fetchone()
                return {
                    'version': row.Version,
                    'level': row.Level,
                    'edition': row.Edition
                }
        except Exception as e:
            print(f"❌ Error getting SQL Server version: {e}")
            return None

    def bulk_insert_csv(self, file_to_insert_abs_path: str, table_name: str, errors_dir, field_terminator='|'):

        file = os.path.basename(file_to_insert_abs_path)

        if not os.path.exists(file_to_insert_abs_path):
            print(f"❌ File not found: {file_to_insert_abs_path}")
            return

        print(f"📄 Importing file: {file_to_insert_abs_path} → Table: {table_name}")

        try:
            with self._connect().cursor() as cursor:
                sql = f"""
                    BULK INSERT [{self.database}].dbo.[{table_name}]
                    FROM '{file_to_insert_abs_path}'
                    WITH (
                        FIELDTERMINATOR = '{field_terminator}',
                        ROWTERMINATOR = '0x0D0A',
                        FIRSTROW = 2,
                        CODEPAGE = '65001',
                        MAXERRORS = 10000,
                        ERRORFILE = '{errors_dir}\\{file}'
                    )
                """
                cursor.execute(sql)
                print(f"✅ Bulk insert completed for {table_name}")
        except Exception as e:
            print(f"❌ Bulk insert failed for {file}: {e}")

            linhas_com_erro = []
            for match in re.finditer(r"row (\d+), column", str(e)):
                linhas_com_erro.append(int(match.group(1)))

            if linhas_com_erro:
                print(f"Linhas com erro detectadas: {linhas_com_erro}")
                erro_csv = os.path.join(errors_dir, f"errors_{file}")
                with (open(file_to_insert_abs_path, encoding="utf-8") as infile,
                      open(erro_csv, "w", newline="", encoding="utf-8") as outfile):
                    reader = csv.reader(infile, delimiter="|")
                    writer = csv.writer(outfile, delimiter="|")
                    header = next(reader)
                    writer.writerow(header)
                    for i, row in enumerate(reader, start=2):
                        if i in linhas_com_erro:
                            writer.writerow(row)
                print(f"Linhas com erro guardadas em: {erro_csv}")



    def recreate_sql_table(self, df: pd.DataFrame, table_name: str):
        """
        Drops and recreates a SQL Server table using pyodbc based on a Pandas DataFrame.
        """
        try:
            with self._connect().cursor() as cursor:
                # DROP TABLE IF EXISTS
                drop_sql = f"IF OBJECT_ID('[{table_name}]', 'U') IS NOT NULL DROP TABLE [{table_name}];"
                cursor.execute(drop_sql)
                print(f"Apagou tabela: {table_name}")

                # CREATE TABLE based on DataFrame
                create_sql = self.generate_create_table(df, table_name)
                cursor.execute(create_sql)
                print(f"✅ Criou tabela SQL: {table_name}")

        except Exception as error:
            print(f"❌ Erro ao criar tabela '{table_name}': {error}")


    def generate_create_table(self, df: pd.DataFrame, table_name: str) -> str:
        type_map = {
            'int64': 'INT',
            'int32': 'INT',
            'float32': 'FLOAT',
            'float64': 'FLOAT',
            'bool': 'BIT',
            'datetime64[ns]': 'DATETIME'
        }

        columns = []
        for col_name, dtype in df.dtypes.items():
            max_len = df[col_name].astype(str).str.len().max()
            sql_type = type_map.get(str(dtype).lower(), f'VARCHAR({max_len})')
            columns.append(f"[{col_name}] {sql_type}")

        columns_def = ",\n  ".join(columns)
        create_sql = f"CREATE TABLE [{table_name}] (\n  {columns_def}\n);"
        return create_sql


    def backup_database(self, backup_dir="backup", stats=5):
        """
        Performs a full backup of the current database to a .bak file.
        """

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        bak_filename = f"{self.database}_{timestamp}.bak"
        file_path = os.path.abspath(os.path.join(backup_dir, bak_filename))

        try:
            with self._connect(db_master=True).cursor() as cursor:
                sql = f"""
                    BACKUP DATABASE [{self.database}] TO DISK = N'{file_path}'
                    WITH COPY_ONLY, NOFORMAT, SKIP, NOREWIND, NOUNLOAD, COMPRESSION, STATS = {stats}
                """
                cursor.execute(sql)

                progress = tqdm(total=100, desc="Backup Progress")
                last_percent = 0

                while cursor.nextset():
                    for message in cursor.messages:
                        msg_text = message[1]
                        match = re.search(r"(\d+)\s+percent\s+processed", msg_text)
                        if match:
                            percent = int(match.group(1))
                            if percent > last_percent:
                                progress.update(percent - last_percent)
                                last_percent = percent

                    cursor.messages.clear()
                progress.close()

                print(f"✅ Backup completed: {file_path}")
        except Exception as e:
            print(f"❌ Error during backup: {e}")

        return file_path  # In case you want to use the path for FTP or cleanup