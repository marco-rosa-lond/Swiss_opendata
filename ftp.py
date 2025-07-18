import io
import os
from dotenv import load_dotenv
import ftplib

load_dotenv("config.env")

FTP_HOST = os.getenv('FTP_HOST')
FTP_PORT = os.getenv('FTP_PORT')
FTP_USER = os.getenv('FTP_USER')
FTP_PASSWORD = os.getenv('FTP_PASSWORD')


def ftp_establish_connection():

    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST, int(FTP_PORT))
    print(ftp.getwelcome())
    ftp.login(FTP_USER, FTP_PASSWORD)

    return ftp


class FtpHandler:

    def __init__(self):
        self.ftp = ftp_establish_connection()

    def create_dir(self, path):
        for dir in path.split("/"):
            if not self.exists(dir):
                self.ftp.mkd(dir)
            self.ftp.cwd(dir)
        self.ftp.cwd("/")

    def exists(self, path):
        try:
            self.ftp.cwd(path)
            self.ftp.cwd("..")
            return True
        except Exception:
            return False


    def send_to_ftp(self, zip_data, dest_dir, filename):
        print(dest_dir)
        self.create_dir(dest_dir)
        self.ftp.cwd(dest_dir)
        self.ftp.storbinary(f'STOR {filename}', zip_data)
        self.ftp.cwd("/")



    def close(self):
        self.ftp.close()