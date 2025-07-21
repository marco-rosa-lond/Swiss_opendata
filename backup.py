from datetime import datetime
import re
import pyodbc
from pyodbc import SQL_DATABASE_NAME
from tqdm import tqdm
from ftp import FtpHandler
from utils import *


backup_dir = "DB_BACKUP"
conn_str = get_connection_string('pyodbc')
master_conn_str = get_connection_string('pyodbc', db_master=True)

def display_backup_progress(cursor):
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


def ftp_save_backup_file(bak_abs_path, ftp_path):
    print(f'\nUploading backup file to {ftp_path}')
    ftp_handler = FtpHandler()
    ftp_handler.send_to_ftp(bak_abs_path, ftp_path)


def drop_database(db_name):

    conn = pyodbc.connect(master_conn_str, autocommit=True)
    try:
        with conn.cursor() as cursor:
            cursor.execute(f"""
            ALTER DATABASE [{db_name}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
            DROP DATABASE IF EXISTS [{db_name}];
            """)
            conn.commit()
            print(f"Database dropped: {db_name}")

    except Exception as e:
        print(f"Error dropping database {db_name}: {e}")

    finally:
        conn.close()


def backup_and_send_with_ftp(ftp_path):
    conn = pyodbc.connect(conn_str, autocommit=True)
    database_name = conn.getinfo(SQL_DATABASE_NAME)

    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    bak_file = f"{database_name}_{timestamp}.bak"
    file_abs_path = os.path.abspath(os.path.join(backup_dir, bak_file))

    stats = '5'

    try:
        with conn.cursor() as cursor:

            sql = f"""
                    BACKUP DATABASE [{database_name}] TO DISK = N'{file_abs_path}'
                    WITH COPY_ONLY, NOFORMAT, SKIP, NOREWIND, NOUNLOAD, COMPRESSION, STATS = {stats}
            """

            cursor.execute(sql)
            display_backup_progress(cursor)
            print(f"Backup of {database_name} database completed")

    except Exception as e:
        print(f"Error creating backup {file_abs_path} file from {database_name}: {e}")
    finally:
        os.remove(file_abs_path)
        conn.close()


    ftp_save_backup_file(file_abs_path, ftp_path)
    drop_database(database_name)








