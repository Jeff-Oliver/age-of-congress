# U.S. Congress Analysis
![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat)

The goal of this project is to create an interactive dashboard to explore congressional demographics in the United States.

## Overview
The bioguide dataset was downloaded as a .zip file containing a file for each member of congress throughout history. This resulted in a dataset of over 13,000 .json files that contained nested data with inconsistent structure between files.\
This inconsistent structure required the use of NoSQL (Not Only SQL) that can handle a non-relational database. MongoDB was chosen as the platform to for extracting the data for visualization.

## Technologies Used

**Core Stack:**
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=flat&logo=mongodb&logoColor=white)

**Tools:**
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=flat&logo=microsoftexcel&logoColor=white)

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

**APIs & Tools:**

- [Geocodio API](https://www.geocod.io/api-to-get-congressional-districts/) - Congressional district lookup
- [JSON Crack](https://marketplace.visualstudio.com/items?itemName=AykutSarac.jsoncrack-vscode) - VS Code extension for visualizing complex JSON structures

## Author

Jeff Oliver

