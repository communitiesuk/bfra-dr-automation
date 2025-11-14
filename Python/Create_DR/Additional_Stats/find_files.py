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
year = dates_variables['year']
month_year = dates_variables['this_month']
month_word = dates_variables['month_word']

ACM_folder = os.path.expanduser(f'~\\OneDrive - MHCLG\\BSP Data and Analysis - Publication of Information\\{year}\\{month_year}\\ACM')
main_folder = os.path.expanduser(f'~\\OneDrive - MHCLG\\BSP Data and Analysis - Publication of Information\\{year}\\{month_year}')

def get_filepath(cut_folder, pattern):
    count = 0
    for file in os.listdir(cut_folder):
        count += 1
        match = re.search(pattern, file)
        if match:
            return match.group()
        #if after searching every file no match is found, raise an error
        elif count == len(os.listdir(cut_folder)):
            raise(FileNotFoundError)



Master_analytical = get_filepath(ACM_folder, r'\d{8} ACM MASTER ANALYTICAL.xlsx')
Portfolio_outputs = get_filepath(main_folder, f'Outputs - Portfolio building list {month_year}.xlsx')
BSF_cut = get_filepath(main_folder, rf"\d{{8}} End {month_word} BSF Data\.xlsx")

