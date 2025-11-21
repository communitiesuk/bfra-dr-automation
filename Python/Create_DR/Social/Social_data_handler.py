# Social_data_handler.py
"""
Created on Monday 29 September 2025, 14:00:49

Author: Matthew Bandura
"""

import pandas as pd
import sys
import os

# Get the directory of the Total script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the Utility folder relative to the script
utility_path = os.path.join(script_dir, 'Utility')

# Add it to sys.path so that python can import from it
sys.path.append(utility_path)

from Utility.functions import chop_df, format_percentage

def Social_retrieve_data_last_quarter(paths_variables):
    print("Handling Last Quarter's Social Data")
    previous_social_path = paths_variables['previous_social_path']
    Social_1 = pd.read_excel(previous_social_path, sheet_name='Social_1')

    Social_1b = chop_df(Social_1, 11, 6)
    Social_1b.rename(columns={Social_1b.columns[-2]: 'Total Number'}, inplace=True)
    Social_1b['Cumulative Number'] = Social_1b['Total Number'].cumsum()

    Social_handled_data_last_quarter = {
        'Social_1b' : Social_1b
    }

    print("DONE!")
    return Social_handled_data_last_quarter

def Social_retrieve_data_last_month(paths_variables):
    print("Handling Last Month's Social Data")
    # Accessing the folder which stores the previous month's MI tables
    previous_tables_path = paths_variables['previous_tables_path']

    # Accessing Social_1
    Social_1 = pd.read_excel(previous_tables_path, sheet_name='Social_1')

    # Transforming Social_1a
    Social_1a = chop_df(Social_1, 3, 6)
    Social_1a.rename(columns={Social_1a.columns[-2]: 'Total Number'}, inplace=True)
    Social_1a['Cumulative Number'] = Social_1a['Total Number'].cumsum()

    # Transforming Social_1b
    Social_1b = chop_df(Social_1, 11, 6)
    Social_1b.rename(columns={Social_1b.columns[-2]: 'Total Number'}, inplace=True)
    Social_1b['Cumulative Number'] = Social_1b['Total Number'].cumsum()
    # Dictionary for transporting dataframes to the next script
    Social_handled_data_last_month = {
        'Social_1a': Social_1a,
        'Social_1b': Social_1b,
    }

    print('DONE!')
    return Social_handled_data_last_month

def Social_retrieve_data_this_month(paths_variables):
    print("Handling This Month's Social Data")
    # Accessing the folder which stores the MI tables
    MI_tables_path = paths_variables['MI_tables_path']
    additional_tables_path = paths_variables['additional_tables_path']

    # Accessing Social_1
    Social_1 = pd.read_excel(MI_tables_path, sheet_name='Social_1')

    # Transforming Social_1a
    Social_1a = chop_df(Social_1, 3, 6)
    Social_1a.rename(columns={Social_1a.columns[2]: '11_18m Percentage', Social_1a.columns[4]: '18m Percentage', Social_1a.columns[-1]: 'Total Percentage', Social_1a.columns[-2]: 'Total Number'}, inplace=True)

    # create two different percentages - ones formatted as strings for the table ('formatted cumulative/total'), one as numbers for calcs
    Social_1a['Cumulative Number'] = Social_1a['Total Number'].cumsum()
    Social_1a['Cumulative Percentage'] = Social_1a['Total Percentage'].cumsum()

    Social_1a['Formatted Cumulative Percentage'] = Social_1a['Cumulative Percentage'].apply(format_percentage)
    Social_1a['Cumulative 11_18m Percentage'] = Social_1a['11_18m Percentage'].cumsum().apply(format_percentage)
    Social_1a['Cumulative 18m Percentage'] = Social_1a['18m Percentage'].cumsum().apply(format_percentage)

    Social_1a['Formatted Total Percentage'] = Social_1a['Total Percentage'].apply(format_percentage)
    Social_1a.at[5, 'Cumulative Number'] = Social_1a.at[5, 'Total Number']

    Social_1a.at[5, 'Formatted Total Percentage'] = "100%"
    Social_1a.at[5, 'Formatted Cumulative Percentage'] = "100%"
    Social_1a.at[4, 'Formatted Cumulative Percentage'] = "100%"

    # Transforming Social_1b
    Social_1b = chop_df(Social_1, 11, 6)
    Social_1b.rename(columns={Social_1b.columns[-1]: 'Total Percentage', Social_1b.columns[-2]: 'Total Number'}, inplace=True)
    Social_1b['Cumulative Number'] = Social_1b['Total Number'].cumsum()
    Social_1b['Cumulative Percentage'] = Social_1b['Total Percentage'].cumsum()
    Social_1b['Formatted Total Percentage'] = Social_1b['Total Percentage'].apply(format_percentage)
    Social_1b['Formatted Cumulative Percentage'] = Social_1b['Cumulative Percentage'].apply(format_percentage)

    # Transforming Social_1c
    Social_1c = chop_df(Social_1, 19, 6)
    Social_1c.rename(columns={Social_1c.columns[-1]: 'Total Percentage', Social_1c.columns[-2]: 'Total Number'}, inplace=True)
    Social_1c['Cumulative Number'] = Social_1c['Total Number'].cumsum()
    Social_1c['Cumulative Percentage'] = Social_1c['Total Percentage'].cumsum()
    Social_1c['Formatted Total Percentage'] = Social_1c['Total Percentage'].apply(format_percentage)
    Social_1c['Formatted Cumulative Percentage'] = Social_1c['Cumulative Percentage'].apply(format_percentage)

    Social_5 = pd.read_excel(MI_tables_path, sheet_name='Social_5')
    Social_5 = chop_df(Social_5, 4, 6)

    # Dictionary for transporting dataframes to the next script
    Social_handled_data_this_month = {
        'Social_1a': Social_1a,
        'Social_1b': Social_1b,
        'Social_1c': Social_1c,
        'Social_5' : Social_5,
        'Social_misc': pd.read_excel(additional_tables_path, sheet_name='Social_misc')
    }
    print('DONE!')

    return Social_handled_data_this_month