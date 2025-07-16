from datetime import datetime
import os
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from tqdm import tqdm


download_folder = 'Downloads'
if not os.path.exists(download_folder):
    os.makedirs(download_folder)


# Stock of all vehicles in circulation
url = "https://opendata.astra.admin.ch/ivzod/1000-Fahrzeuge_IVZ/1300-Fahrzeugbestaende/1320-Datensaetze_monatlich/BEST.txt"
filename = url.split('/')[-1]



def fetch_data_with_retry(retries=3):
    """
    Fetches data from a URL with retry mechanism in case of ReadTimeout error,
    and displays a progress bar while downloading.
    """
    session = requests.Session()
    retry_strategy = Retry(
        total=retries,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    filepath = os.path.join(download_folder, filename.replace('.txt', '.csv'))


    try:
        with session.get(url, stream=True, timeout=(30, 120)) as r:
            r.raise_for_status()

            # add data ultima modificação ao nome do ficheiro
            response_last_modified_dt = datetime.strptime(r.headers.get('Last-Modified'), '%a, %d %b %Y %H:%M:%S %Z')
            last_modified = str(response_last_modified_dt.strftime('%Y-%m-%d'))
            filepath = filepath.split('.csv')[0] + f"-{last_modified}" + '.csv'


            file_size_in_bytes = int(r.headers.get('Content-Length', 0))
            print(f"File size: {str(round(file_size_in_bytes/1024**3,2))} GB")

            if os.path.exists(filepath) and file_size_in_bytes == os.path.getsize(filepath):
                print(f"{filepath.split('\\')[1]} already exists, skipping.")
                return None


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

    return None




def download_datasets():
    fetch_data_with_retry()