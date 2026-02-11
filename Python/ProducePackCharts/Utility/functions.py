# functions.py
"""
Created on Wednesday 21 May 2025, 13:49:16

Author: Harry Simmons
"""

import re
import os
import pandas as pd
import calendar as cal


def chop_df(df, top_rows_to_drop, bottom_rows_to_drop):
    # Drop rows from 0 to num_rows_to_drop - 1
    df = df.drop(range(top_rows_to_drop))

    # Reset the index
    df = df.reset_index(drop=True)

    # Promote the next row to be the headers
    df.columns = df.iloc[0]
    df = df.drop(0).reset_index(drop=True)

    # Drop bottom rows if bottom_rows_to_drop is not None
    if bottom_rows_to_drop is not None:
        df = df.iloc[:bottom_rows_to_drop]

    return df

def get_excel_path(folder_path):
    files = os.listdir(folder_path)
    excel_files = [file for file in files if file.endswith('.xlsx') or file.endswith('.xls') or file.endswith('.xlsm')]
    if len(excel_files) == 1:
        excel_path = os.path.join(folder_path, excel_files[0])
        return excel_path
    else:
        raise FileNotFoundError("No Excel file found in the folder.")
    

def create_paths():
    # Build the path to the graph output folder
    figure_path = r'Q:\BSP\Automation\DR Automation\DR_outputs\DR_graphs'

    previous_MI_folder = r'Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT MI TABLES HERE]\[LAST MONTHS MI TABLES]'
    previous_tables_path = get_excel_path(previous_MI_folder)

    MI_folder = r"Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT MI TABLES HERE]"
    MI_tables_path = get_excel_path(MI_folder)

    additional_folder = r'Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT ADDITIONAL DR STATS HERE]\[AUTOMATION]'
    additional_tables_path = get_excel_path(additional_folder)

    combined_folder = r'Q:\BSP\Automation\MI Tables\Combined'
    combined_ts_path = get_excel_path(combined_folder)



    partial_output_path = r'Q:\BSP\Automation\DR Automation\DR_outputs\DR_graphs'

    save_path = r'Q:\BSP\Automation\DR Automation\DR_outputs\Auto_DR'

    dummy_tables_folder = r"Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT MI TABLES HERE]\[DUMMY DATA]"
    dummy_tables_path = get_excel_path(dummy_tables_folder)
    paths = {'figure_path' : figure_path,
             'previous_tables_path' : previous_tables_path,
             'MI_tables_path' : MI_tables_path,
             'additional_tables_path' : additional_tables_path,
             'save_path' : save_path,
             'combined_ts_path' : combined_ts_path,
             'partial_output_path' : partial_output_path,
             'dummy_tables_path' : dummy_tables_path
    }
    return paths


paths_variables = create_paths()
MI_tables_path = paths_variables['MI_tables_path']


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

    # Convert month name to number
    month = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }.get(month_word, None)
    
    #this ensures the dictionary returns appropriately named variables
    sheet_prefix = sheet_name[:3].lower()

    # Get last day of the month - monthrange returns the first weekday (ignored by _) and the final day (given to last_day)
    _, last_day = cal.monthrange(year, month)
    if sheet_name == 'Cover':
        return {
            "last_day": last_day,
            "year": year,
            "month": month,
            "month_word" : month_word }
    else:
        return {
            f'{sheet_prefix}_last_day' : last_day,
            f'{sheet_prefix}_year' :  year,            
            f"{sheet_prefix}_month": month 
        }

def sort_dates():
    print('Handling Dates')
    # extract the current DR month and year
    cover_info = extract_month_year('Cover', MI_tables_path)
    month, month_word, year, last_day = cover_info['month'], cover_info['month_word'], cover_info['year'], cover_info['last_day']


    print('DONE!')
    return month, year
