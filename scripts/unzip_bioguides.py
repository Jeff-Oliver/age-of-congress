# import dependencies
import pandas as pd
import zipfile
import json
from pathlib import Path

# Unzip the dataset using zipfile

# Define the path to the zip file and the extraction directory
zip_file_path = 'data\\external\\BioguideProfiles.zip'

# Define the extraction directory
extraction_dir = "D:\\bioguides" # Set to your desired extraction path

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_dir)

# calculate size of the extracted folder
extracted_size = sum(f.stat().st_size for f in
                     Path(extraction_dir).rglob('*')if f.is_file())
print(f'Total size of extracted folder: {extracted_size / (1024 * 1024):.2f} MB')

# Make a list of all the json files in the extracted directory
json_files = list(Path(extraction_dir).rglob('*.json'))
print(f'Number of JSON files found: {len(json_files)}')