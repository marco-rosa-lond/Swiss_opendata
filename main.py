
from download import download_datasets
from backup import backup_and_send_with_ftp


# BEST (PARQUE SUIÇA | MENSAL)
# NEUZU (NOVOS REGISTOS | BISEMANAL)

FILE_URLS = {
    "BEST" : "https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1300-Fahrzeugbestaende/1320-Datensaetze_monatlich/BEST.txt",
    "NEUZU" : "https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1200-Neuzulassungen/1210-Datensaetze_monatlich/NEUZU.txt"
}

#NEUZU
# January includes the new registrations of the entire previous year.Otherwise, the new registrations are included since the beginning of the year.
# All details refer to the time when the data set was created and not the date of initial registration.


ftp_path = '/FILES/__PROJECT__/BACKUPS'

def main():

    # Step 1 - download files
    download_datasets(FILE_URLS)

    # Step 3 - Backup the database to ftp destination
    backup_and_send_with_ftp(ftp_path)


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