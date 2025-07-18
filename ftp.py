import io
import os
from dotenv import load_dotenv
import ftplib



def ftp_establish_connection():

    load_dotenv("config.env")
    host = os.getenv('FTP_HOST')
    port = os.getenv('FTP_PORT')
    user = os.getenv('FTP_USER')
    password = os.getenv('FTP_PASSWORD')

    ftp = ftplib.FTP()
    ftp.connect(host, int(port))
    print(ftp.getwelcome())
    ftp.login(user, password)

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