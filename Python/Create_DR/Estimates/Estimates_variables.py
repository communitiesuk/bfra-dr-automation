# Estimates_variables.py
"""
Created on Monday 27 January 2025, 09:14:43

Author: Harry Simmons
"""

import pandas as pd

from Utility.functions import format_percentage

def Estimates_variable_creator(Portfolio_handled_data):
    # Unpacking dataframes from Portfolio_data_handler
    Combined_2 = Portfolio_handled_data['Combined_2a']

    Estimates_tables_number_of_buildings = pd.DataFrame({
        'Height': ['11-18m ', '18m+', 'Total 11m+'],
        'Low Estimate': [2800, 3000, 5700],
        'High Estimate': [5400, 3200, 8600],
    })

    Estimates_tables_proportion_of_buildings = pd.DataFrame({
        'Height': ['11-18m ', '18m+', 'Total 11m+'],
        'Number of buildings currently monitored': [Combined_2.loc[3, '11_18m Number'], Combined_2.loc[3, '18m Number'], Combined_2.loc[3, 'Current Number']],
        'As a proportion of the low estimate': [format_percentage(Combined_2.loc[3, '11_18m Number']/2772), format_percentage(Combined_2.loc[3, '18m Number']/2951), format_percentage(Combined_2.loc[3, 'Current Number']/5723)],
        'As a proportion of the high estimate': [format_percentage(Combined_2.loc[3, '11_18m Number']/5385), format_percentage(Combined_2.loc[3, '18m Number']/3199), format_percentage(Combined_2.loc[3, 'Current Number']/8584)]
    })
    
    Estimates_tables = {
        'Estimates_tables_proportion_of_buildings' : Estimates_tables_proportion_of_buildings,
        'Estimates_tables_number_of_buildings' : Estimates_tables_number_of_buildings
    }

    Estimates_headline_dict = {
        'Estimates_11m_proportion_of_low_estimate': format_percentage(Combined_2.loc[3, 'Current Number']/5723),
        'Estimates_11m_proportion_of_high_estimate': format_percentage(Combined_2.loc[3, 'Current Number']/8584).replace('%', '')
    }

    Estimates_section_dict = {
        'Estimates_11m_proportion_of_low_estimate': format_percentage(Combined_2.loc[3, 'Current Number']/5723),
        'Estimates_11m_proportion_of_high_estimate': format_percentage(Combined_2.loc[3, 'Current Number']/8584).replace('%', '')
    }

    return Estimates_tables, Estimates_headline_dict, Estimates_section_dict
