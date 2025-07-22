import os
import re
import time
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
import pandas as pd

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


# Step 2: Extract dates and build a list of (filename, date) tuples
def extract_date(filename):
    match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
    if match:
        return datetime.strptime(''.join(match.groups()), '%Y-%m-%d')
    return None
