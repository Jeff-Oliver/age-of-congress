# U.S. Congress Analysis

![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat)

## Overview

This project aims to explore how the age demographic in the U.S. Congress has chnaged over time. This information is typically made from the average ages on the start date of a congressional term. I would like a more granular view, down to the day. This will mean accounting for partial terms and party changes. Partial terms can arise from a number of factors, but primarily it's resignations and appointments. The end goal is to construct an interactive dashboard that can analyze age in the House and Senate as well as party affilitaion.

Future work would include adding gender and religion to this analysis.

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
├── data/
│   ├── external/       # Original Dataset
│   ├── raw/            # Extracted Data for cleaning
│   ├── processed/      # Cleaned data ready for analysis
│   └── tableau/        # tableau files
├── notebooks/          # notebook files for data cleaning
├── scripts/            # python scripts for data prep
├── tests/              # Test files
├── requirements.txt
└── README.md
```

## Project Walkthrough

The bioguide dataset was [downloaded](https://bioguide.congress.gov/search) as a .zip file. This is a collection of .json files with one file for each member of Congress. The extracted folder contains over 13,000 .json files with nested data and inconsistent structure between files.

This inconsistent structure required the use of NoSQL (Not Only SQL) that can handle a non-relational database. MongoDB was selected as the platform for data extraction.

The number of congresses to include in this analysis was the 90th to present day. This range was selected because it is after Hawaii and Alaska were admitted into the union and standardizes to the current makeup of the United States. No Dakota Territory worry about &#128521;

Term start and end dates do not always align with the start and end dates of the congress itself. Member would join at non-standard dates by resignation, dying, special elections or appointments. The reason for these non-standard dates is most often found in the member's bioguide biography. Extracting this data using an AI model resulted in unacceptable errors which were not included here.

These edge cases were manually updated by using Excel and the bioguide information in an unfortunate brute force method. There were several errors in the original dataset. The majority of errors were found in the "jobPositions.startDate" field.

### Three tables were assembled

```
1. Profiles - list of members and basic data about them
2. Postings - every member posting in each congress evaluated
3. Sessions - The start and end dates of each congressional setting
```

While cleaning the postings data, 18 members were found to have switched parties. This data was flattened to have a new row showing the dates served to each party.

A data error was found during exploration. The start date of the first congress served would be found in the start date of the final term served.

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Install [MongoDB Community Edition](https://www.mongodb.com/try/download/community)

## Usage

1. Run `scripts/unzip_bioguides.py` to unzip datafile
2. Use MongoDB to create a database
3. Connect MongoDB to database
4. Run `scripts/mongo_connect.py` to connect to MongoDB
5. Use `notebooks/data_table_builder.ipynb` to extract data to .csv files
6. Clean the data
    1. Run `notebooks/cleaning_postings.ipynb` - do this before cleaning profiles, this code reduces the number of profiles required.
    2. Run `notebooks/cleaning_profiles.ipynb`
7. Analyze in Tableau

## Helpful Resources

**Data Sources:**

- [Bioguide Data](https://bioguide.congress.gov) - Official congressional biographical directory
- [Congress Legislators GitHub](https://github.com/unitedstates/congress-legislators) - Structured congressional data

**APIs**

- [Geocodio API](https://www.geocod.io/api-to-get-congressional-districts/) - Congressional district lookup


## Author

Jeffrey Oliver

