# Costs_variables.py
"""
Created on Monday 22nd December 2025, 14:36:06

Author: Matthew Bandura
"""

import pandas as pd 

def Costs_variable_creator(Costs_handled_data):
    # Unpacking dataframes from Costs_data_handler
    Estimated_5 = Costs_handled_data['Estimated_5']
    Estimated_6 = Costs_handled_data['Estimated_6']
    Estimated_7 = Costs_handled_data['Estimated_7']



    Costs_section_dict = {
    'Costs_total_low' : Estimated_5.loc[2, 'Low Estimate'],
    'Costs_total_high' : Estimated_5.loc[2, 'High Estimate'],

    'Costs_gvt_low_pct' : Estimated_6.loc[0, 'Formatted Low Estimate'],
    'Costs_gvt_high_pct' : Estimated_6.loc[0, 'Formatted High Estimate'],
    'Costs_gvt_low' : Estimated_5.loc[0, 'Low Estimate'],
    'Costs_gvt_high' : Estimated_5.loc[0, 'High Estimate'],

    'Costs_other_high' : Estimated_5.loc[1, 'Low Estimate'],
    'Costs_other_low' : Estimated_5.loc[1, 'High Estimate'],
    'Costs_other_low_pct' : Estimated_6.loc[1, 'Formatted Low Estimate'],
    'Costs_other_high_pct' : Estimated_6.loc[1, 'Formatted High Estimate'],

    'Costs_total_available' : Estimated_7.loc[3, 'Estimate'],
    'Costs_exchequer' : Estimated_7.loc[0, 'Estimate'],
    'Costs_developer' : Estimated_7.loc[1, 'Estimate'],
    'Costs_BSL' : Estimated_7.loc[2, 'Estimate']
    }
    
    Costs_estimates_table = pd.DataFrame({
        'Funding Source': ['Government Programmes', 'Non-government actors', 'Total'],
        'Low Estimate': Estimated_5['Low Estimate'],
        'Central Estimate': Estimated_5['Central Estimate'],
        'High Estimate': Estimated_5['High Estimate'],
    })

    Costs_proportions_table = pd.DataFrame({
        'Funding Source': ['Government Programmes', 'Non-government actors', 'Total'],
        'Low Estimate': Estimated_6['Formatted Low Estimate'],
        'Central Estimate': Estimated_6['Formatted Central Estimate'],
        'High Estimate': Estimated_6['Formatted High Estimate'],
    })


    Costs_tables = {
        'Costs_estimates_table' : Costs_estimates_table, 
        'Costs_proportions_table' : Costs_proportions_table
    }



    return Costs_tables, Costs_section_dict
