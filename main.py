
from download import download_datasets
from ftp import FtpHandler
from SQLServer import SQLServerManager
from utils import create_directory, drop_directory
# from restore import restore_last_database_backup

# BEST (PARQUE SUIÇA | MENSAL)
# NEUZU (NOVOS REGISTOS | BISEMANAL)

#NEUZU
# January includes the new registrations of the entire previous year.Otherwise, the new registrations are included since the beginning of the year.
# All details refer to the time when the data set was created and not the date of initial registration.

FILE_URLS = {
    "BEST" : "https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1300-Fahrzeugbestaende/1320-Datensaetze_monatlich/BEST.txt",
    "NEUZU" : "https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1200-Neuzulassungen/1210-Datensaetze_monatlich/NEUZU.txt"
}

ftp_path = '/FILES/__PROJECT__/BACKUPS' # Change to NAS backup folder path

downloads_dir = 'downloads'
backup_dir = "backups"


def main():

    sql_manager = SQLServerManager()

    try:
        # Re-create de database
        sql_manager.recreate_database()

        # Step 1 - download files
        for dataset_name, url in FILE_URLS.items():
            download_datasets(dataset_name, url)

        # Step 3 - Backup the database to ftp destination
        create_directory(backup_dir)
        bak_file_path = sql_manager.backup_database(backup_dir)

        ftp_handler = FtpHandler()
        ftp_handler.send_to_ftp(bak_file_path, ftp_path)

    finally:
        sql_manager.drop_database()
        drop_directory(backup_dir)



if __name__ == '__main__':
    try:
        main()
        print('Done')
    except Exception as e:
        print("An error occurred:",
              e)
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")