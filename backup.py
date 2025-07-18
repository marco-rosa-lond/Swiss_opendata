from datetime import datetime
import re
import pyodbc
from pyodbc import SQL_DATABASE_NAME
from tqdm import tqdm
from ftp import FtpHandler
from utils import *

conn_str = get_connection_string('pyodbc')
backup_dir = "DB_BACKUP"

def get_backup_progress(cursor):
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


def ftp_save_backup_file(file_abs_path, ftp_path):
    bak_file = os.path.basename(file_abs_path)
    print(f'Sending backup file to {ftp_path}/{bak_file}')
    input('Continue?')

    ftp_handler = FtpHandler()
    try:

        with open(file_abs_path, "rb") as bak_file_bin:
            ftp_handler.send_to_ftp(
                zip_data=bak_file_bin,
                dest_dir=ftp_path,
                filename=bak_file
            )

        print("BACKUP SENT TO FTP")
    except Exception as e:
        print(e)

    finally:
        ftp_handler.close()


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
            get_backup_progress(cursor)
        conn.close()

        ftp_save_backup_file(file_abs_path, ftp_path)

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        os.remove(file_abs_path)
        conn.close()



