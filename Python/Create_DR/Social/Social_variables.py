# Social_variables.py
"""
Created on Monday 29 September 2025, 14:00:49

Author: Matthew Bandura
"""

import pandas as pd

from Utility.functions import Change_line_in_DR, format_percentage

def Social_variable_creator(Social_handled_data_this_month, Social_handled_data_last_month):

    # Unpack last months dfs
    Social_1a_last_month = Social_handled_data_last_month['Social_1a']
    Social_1b_last_month = Social_handled_data_last_month['Social_1b']

    # Unpack this months dfs
    Social_1a_this_month = Social_handled_data_this_month['Social_1a']
    Social_1b_this_month = Social_handled_data_this_month['Social_1b']


    # Format the table for social remediation progress
    Social_remediation_table = pd.DataFrame({
        'Remediation Stage': ['Remediation completed', 'Works started', 'Works not started', 'Remediation progress currently unknown', 'Total'],
        'Number': Social_1b_this_month['Total Number'],
        'Percentage': Social_1b_this_month['Formatted Total Percentage'],
        'Cumulative Number': Social_1b_this_month['Cumulative Number'],
        'Cumulative Percentage': Social_1b_this_month['Formatted Cumulative Percentage']
    })
    
    Social_tables = {
        'Social_remediation_table' : Social_remediation_table
    }

    Social_headline_dict = {
        'Social_self_funded_total': format(Social_1b_this_month.loc[4, 'Total Number'], ','),
        'Social_self_funded_total_change': Change_line_in_DR(Social_1b_this_month.loc[4, 'Total Number'] - Social_1b_last_month.loc[4, 'Total Number']),

        'Social_self_funded_started_no': format(Social_1b_this_month.loc[0, 'Cumulative Number'], ','),
        'Social_self_funded_started_pct': Social_1b_this_month.loc[0, 'Formatted Cumulative Percentage'],
        'Social_self_funded_started_change': Change_line_in_DR(Social_1b_this_month.loc[0, 'Cumulative Number'] - Social_1b_this_month.loc[0, 'Cumulative Number']),
    }
    

    Social_section_dict = {
        'Social_total_no': format(Social_1b_this_month.loc[4, 'Total Number'], ','),
        'Social_total_change': Change_line_in_DR(Social_1b_this_month.loc[4, 'Total Number'] - Social_1b_last_month.loc[4, 'Total Number']),

        'Social_started_no': format(Social_1b_this_month.loc[1, 'Cumulative Number'], ','),
        'Social_started_pct': Social_1b_this_month.loc[1, 'Formatted Cumulative Percentage'],
        'Social_started_change': Change_line_in_DR(Social_1b_this_month.loc[1, 'Cumulative Number'] - Social_1b_last_month.loc[1, 'Cumulative Number']),

        'Social_completed_no': format(Social_1b_this_month.loc[0, 'Cumulative Number'], ','),
        'Social_completed_pct': Social_1b_this_month.loc[0, 'Formatted Cumulative Percentage'],
        'Social_completed_change': Change_line_in_DR(Social_1b_this_month.loc[0, 'Cumulative Number'] - Social_1b_last_month.loc[0, 'Cumulative Number']),

        'Social_not_started_no' : format(Social_1b_this_month.loc[2, 'Total Number'] + Social_1b_this_month.loc[3, 'Total Number'], ','),
        'Social_not_started_pct' : format_percentage(Social_1b_this_month.loc[2, 'Total Percentage'] + Social_1b_this_month.loc[3, 'Total Percentage']),
        'Social_not_started_change' : Change_line_in_DR((Social_1b_this_month.loc[2, 'Total Number'] + Social_1b_this_month.loc[3, 'Total Number']) - (Social_1b_last_month.loc[2, 'Total Number'] + Social_1b_last_month.loc[3, 'Total Number'])),

        'Social_unknown_no' : format(Social_1b_this_month.loc[3, 'Total Number'], ','),
        'Social_unknown_pct' : Social_1b_this_month.loc[3, 'Formatted Total Percentage'],

        'Social_SF_18m_starts_pct' : Social_1b_this_month.loc[1, 'Cumulative 18m Percentage'],
        'Social_SF_11m_starts_pct' : Social_1b_this_month.loc[1, 'Cumulative 11_18m Percentage'],
    }
    return Social_tables, Social_headline_dict, Social_section_dict
