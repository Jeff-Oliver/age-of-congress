# U.S. Congress Analysis
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat)

The goal of this project is to create an interactive dashboard to explore congressional demographics in the United States.

## Overview
The bioguide dataset was [downloaded](https://bioguide.congress.gov/search) as a .zip file. This is a collection of .json files with one file for each member of Congress. The extracted folder contains over 13,000 .json files with nested data and inconsistent structure between files.

This inconsistent structure required the use of NoSQL (Not Only SQL) that can handle a non-relational database. MongoDB was selected as the platform for data extraction.

The number of congresses to include in this analysis was the 90th to present day. This range was selected because it is after Hawaii and Alaska were admitted into the union and standardizes to the current makeup of the United States. No Dakota Territory worry about &#128521;

Term start and end dates do not always align with the start and end dates of the congress itself. Member would join at non-standard dates by resignation, dying, special elections or appointments. The reason for these non-standard dates is most often found in the member's bioguide biography. Extracting this data using an AI model resulted in unacceptable errors which were not included here.

These edge cases were manually updated by using Excel and the bioguide information in an unfortunate brute force method. There were several errors in the original dataset. The majority of errors were found in the "jobPositions.startDate" field.

## Technologies Used

**Core Stack:**
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat&logo=mongodb&logoColor=white)

**Tools:**
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-1E4C7A?style=flat&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=flat&logo=microsoftexcel&logoColor=white)
![JSON Crack](https://img.shields.io/badge/JSON%20Crack-000000?style=flat&logo=json&logoColor=white)

## Project Structure

```bash
AGE-OF-CONGRESS/
├── src/               # Source code
├── data/              # Raw and processed data
│   ├── raw/
│   └── processed/
├── output/            # Generated outputs
├── tests/             # Test files
├── database_builder.ipynb
├── requirements.txt
└── README.md
```
## Project Walkthrough

1. Unzip the bioguide.zip file (unzip_json.ipynb can be used here)
2. Connect the unzipped folder to MongoDB
3. Run import_bioguide.py to import data from MongoDB (note this can take a minute to complete)
4. Build the database using database_builder.ipynb

**The following tables were extracted for analysis:**

1. **sessions.csv** - List of congressional sessions assembled in Excel
2. **profiles.csv** - List of all bioguide_id's and basic info (took 2.5 minutes to run)
3. **postings.csv** - List of congressional postings, including start and end dates

While cleaning the postings data, 18 members were found to have switched parties. This data was flattened to have a new row showing the dates served to each party.

A data error was found during exploration. The start date of the first congress served would be found in the start date of the final term served.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up MongoDB connection
4. Run the import script: `python import_bioguide.py`

## Usage

1. Import bioguide data: `python import_bioguide.py`
2. Analyze data: Open and run `database_builder.ipynb`
3. View outputs in the `output/` folder

## Helpful Resources

**Data Sources:**

- [Bioguide Data](https://bioguide.congress.gov) - Official congressional biographical directory
- [Congress Legislators GitHub](https://github.com/unitedstates/congress-legislators) - Structured congressional data

**APIs**

- [Geocodio API](https://www.geocod.io/api-to-get-congressional-districts/) - Congressional district lookup


## Author

Jeff Oliver

