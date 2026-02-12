'''
Author: Matthew Bandura
Created on Thursday 23rd October, 09:09:50    
'''
# setup initial imports and pull in dates to create dynamic filepaths linking to latest Sharepoint folder

import os
import re
import sys
# setup Utility as a package from which the dates module can be imported
parent_path = os.path.abspath(os.path.join(os.getcwd(), '..'))
sys.path.append(parent_path)

from Utility.dates import sort_dates

dates_variables = sort_dates()

#function which matches files in a folder to a regex pattern
def get_filepath(cut_folder, pattern):
    count = 0
    for file in os.listdir(cut_folder):
        count += 1
        #go through every filename and check it for a match with the regex pattern
        match = re.search(pattern, file)
        if match:
            #return the filename if a match is found
            return match.group()
        #if after searching every file no match is found, raise an error
        elif count == len(os.listdir(cut_folder)):
            raise(FileNotFoundError)

#function to generate the full paths to the files we need so the workbooks can be loaded
def generate_filepaths():
    year = dates_variables['year']
    month_year = dates_variables['this_month']
    month_word = dates_variables['month_word']
    last_month_year = dates_variables['last_month_year']
    last_month = dates_variables['last_month']



    ACM_folder = os.path.expanduser(f'~\\OneDrive - MHCLG\\BSP Data and Analysis - Publication of Information\\{year}\\{month_year}\\ACM')
    main_folder = os.path.expanduser(f'~\\OneDrive - MHCLG\\BSP Data and Analysis - Publication of Information\\{year}\\{month_year}')
    previous_folder = os.path.expanduser(f'~\\OneDrive - MHCLG\\BSP Data and Analysis - Publication of Information\\{last_month_year}\\{last_month}' + ' ' + f'{last_month_year}')

    Master_analytical = get_filepath(ACM_folder, r'\d{8} ACM MASTER ANALYTICAL.xlsx')
    CSS_data = get_filepath(main_folder, f'CSS data end {month_word}.xlsx')
    BSF_cut = get_filepath(main_folder, rf"\d{{8}} End {month_word} BSF Data\.xlsx")
    last_month_BSF_cut = get_filepath(previous_folder, rf"\d{{8}} End {last_month} BSF Data\.xlsx")

    # MI_tables_path = rf'Q:\BSP\Automation\DR Automation\Excel_inputs\[PUT MI TABLES HERE]\Building Safety Remediation Tables {month_word} {year}.xlsm'

    Master_analytical_path = ACM_folder + f'\\{Master_analytical}'
    CSS_data_path = main_folder + f'\\{CSS_data}'
    BSF_cut_path = main_folder + f'\\{BSF_cut}'
    last_month_BSF_cut_path = previous_folder + f'\\{last_month_BSF_cut}'
    return Master_analytical_path, BSF_cut_path, last_month_BSF_cut_path, CSS_data_path, month_word

