#Costs_data_handler.py
"""
Created on Monday 22nd December 2025 14:12:21

Author: Matthew Bandura
"""

import pandas as pd
import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the Utility folder relative to the script
utility_path = os.path.join(script_dir, 'Utility')

# Add it to sys.path so that python can import from it
sys.path.append(utility_path)

from Utility.functions import chop_df

def Costs_retrieve_data(paths_variables):
    print('Handling Costs Data')

    # Accessing the folder which stores the MI tables
    MI_tables_path = paths_variables['MI_tables_path']

    # Accessing and transforming Estimated_5 (funding source by height and actor)
    Estimated_5 = pd.read_excel(MI_tables_path, sheet_name='Estimated_5')
    Estimated_5 = chop_df(Estimated_5, 14, 3)
    Estimated_5.rename(columns={Estimated_5.columns[-1]: 'High Estimate', Estimated_5.columns[-2]: 'Central Estimate', Estimated_5.columns[-3]: 'Low Estimate'}, inplace=True)
   
    #Accessing and transforming Estimated_6 (percentages of funding source)
    Estimated_6 = pd.read_excel(MI_tables_path, sheet_name='Estimated_6')
    Estimated_6 = chop_df(Estimated_6, 3, 4)
    Estimated_6.rename(columns={Estimated_6.columns[-1]: 'High Estimate', Estimated_6.columns[-2]: 'Central Estimate', Estimated_6.columns[-3]: 'Low Estimate'}, inplace=True)


    #Accessing and transforming Estimated_7 (for sources of gvt funding)
    Estimated_7 = pd.read_excel(MI_tables_path, sheet_name='Estimated_7')
    Estimated_7 = chop_df(Estimated_7, 3, 4)


    Costs_handled_data = {
        'Estimated_5': Estimated_5,
        'Estimated_6': Estimated_6,
        'Estimated_7': Estimated_7
    }

    print('DONE!')
    return Costs_handled_data
