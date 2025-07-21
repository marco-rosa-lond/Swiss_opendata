
import traceback
import pyodbc
from utils import *
from ftp import *

backup_dir = "DB_BACKUP"
master_conn_str = get_connection_string('pyodbc', db_master=True)


def get_mssql_data_path(conn):

    with conn.cursor() as cursor:
        cursor.execute("SELECT SERVERPROPERTY('InstanceDefaultDataPath')")
        datapath = cursor.fetchone()
        return datapath[0]

def download_last_backup_from_network_loc(ftp_path):
    ftp_handler = FtpHandler()
    bak_files = ftp_handler.list_files_in_dir(ftp_path, '.bak')

    if not bak_files:
        print(f"No backup files found in {ftp_path}")
        return

    # Find the last backup file
    files_with_dates = [(f, extract_date(f)) for f in bak_files if extract_date(f) is not None]
    most_recent_file = max(files_with_dates, key=lambda x: x[1])[0]
    print("last database backup: {}".format(most_recent_file))

    # Download file
    ftp_handler.download_from_ftp(most_recent_file, backup_dir)
    downloaded_file_path = os.path.join(backup_dir, most_recent_file)
    return downloaded_file_path


def restore_last_database_backup(ftp_path):

    print("\n Restoring database..")
    bak_file_path = download_last_backup_from_network_loc(ftp_path)
    bak_file_abs_path = os.path.abspath(bak_file_path)

    conn = pyodbc.connect(master_conn_str, autocommit=True)

    try:
        # Get MSSQL Data path
        mssql_data_path = get_mssql_data_path(conn)

        with conn.cursor() as cursor:

            # Step 1: Get logical names (.mdf file name & .log file name) from the BAK file
            filelist_sql = fr"""
                   RESTORE FILELISTONLY
                   FROM DISK = N'{bak_file_abs_path}'
                   """

            cursor.execute(filelist_sql)
            filelist = cursor.fetchall()

            mdf_logical_name = filelist[0][0]
            log_logical_name = filelist[1][0]
            target_db = mdf_logical_name

            # Step 2: Build the restore command
            data_path = rf'{mssql_data_path}{target_db}.mdf'  # Change to desired data file path
            log_path = rf'{mssql_data_path}{target_db}_log.ldf'  # Change to desired log file path

            restore_sql = f"""
               RESTORE DATABASE [{target_db}]
               FROM DISK = N'{bak_file_abs_path}'
               WITH MOVE N'{mdf_logical_name}' TO N'{data_path}',
                    MOVE N'{log_logical_name}' TO N'{log_path}',
                    REPLACE;
               """

            # Step 3: Execute restore
            cursor.execute(restore_sql)

            print(f"Database '{target_db}' restored successfully.")

    except pyodbc.Error as e:
        print("Database operation failed:")
        print(e)
        traceback.print_exc()

    except Exception as e:
        print("An unexpected error occurred:")
        print(e)
        traceback.print_exc()

    finally:
        # Remove the BAK file
        try:
            if os.path.exists(bak_file_abs_path):
                os.remove(bak_file_abs_path)
                print(f"Deleted backup file: {bak_file_abs_path}")
        except Exception as file_err:
            print(f"Failed to delete backup file: {bak_file_abs_path}")
            print(file_err)

            conn.close()







