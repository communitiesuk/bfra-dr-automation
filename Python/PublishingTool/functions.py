# functions.py
"""
Created on Tuesday 23 September 2025, 16:43:16

Author: Matthew Bandura
"""

import os
import pandas as pd
import re

def get_excel_path(folder_path):
    files = os.listdir(folder_path)
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls') or file.endswith('.xlsm')]
    if len(excel_files) == 1:
        excel_path = os.path.join(folder_path, excel_files[0])
        return excel_path
    else:
        raise FileNotFoundError("No Excel file found in the folder.")
    
def extract_month_year(sheet_name, file_path):
    #Extracts month and year from the first column header of a given Excel sheet using regex searches.
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    title = df.columns[0]

    # Extract year
    year_match = re.search(r'\b\d{4}\b', title)
    year = int(year_match.group()) if year_match else None

    # Extract month
    month_match = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\b', title)
    month_word = month_match.group() if month_match else None

    return month_word, year
    


def create_paths():
    MI_folder = r"Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT MI TABLES HERE]"
    MI_tables_path = get_excel_path(MI_folder)

    # extract the current DR month and year
    this_month, this_year = extract_month_year('Cover', MI_tables_path)

    md_path =f'Q:\\BSP\\Automation\\DR Automation\\DR_outputs\\DR_markdown\\Building Safety Release {this_month} {this_year} - Markdown version.md'

    docx_path = f'Q:\\BSP\\Automation\\DR Automation\\DR_outputs\\Auto_DR\\Building Safety Release {this_month} {this_year}.docx'

    paths = {'docx_path' : docx_path,
             'md_path' : md_path,
    }
    return paths

