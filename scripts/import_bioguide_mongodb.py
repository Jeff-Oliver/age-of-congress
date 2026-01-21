# Import Dependencies
from pymongo import MongoClient
import json
import glob

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client["bioguide"]         # Database Name
collection = db["profiles"]     # Collection Name

# Folder path to JSON files
folder_path = r"D:\bioguides\*.json"

# Loop through all JSON files and import
count = 0
for filename in glob.glob(folder_path):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        collection.insert_one(data)
        count += 1

print(f"Imported {count} files")
