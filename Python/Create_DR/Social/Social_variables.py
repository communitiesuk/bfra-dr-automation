# Social_variables.py
"""
Created on Monday 29 September 2025, 14:00:49

Author: Matthew Bandura
"""

import pandas as pd

from Utility.functions import Change_line_in_DR, format_percentage

def Social_variable_creator(Social_handled_data_last_quarter, Social_handled_data_this_month, Social_handled_data_last_month):
    
    Social_1b_last_quarter = Social_handled_data_last_quarter['Social_1b']
    # Unpack last months dfs
    Social_1a_last_month = Social_handled_data_last_month['Social_1a']
    Social_1b_last_month = Social_handled_data_last_month['Social_1b']

    # Unpack this months dfs
    Social_1a_this_month = Social_handled_data_this_month['Social_1a']
    Social_1b_this_month = Social_handled_data_this_month['Social_1b']
    Social_1c_this_month = Social_handled_data_this_month['Social_1c']
    Social_misc = Social_handled_data_this_month['Social_misc']


    # Format the table for social remediation progress
    Social_remediation_table = pd.DataFrame({
        'Remediation Stage': ['Remediation complete', 'Remediation complete – awaiting building control sign-off', 'Remediation started', 'Remediation works planned', 'Remediation plans unclear from survey', 'Formatted Total Percentage'],
        'Number': Social_1a_this_month['Total Number'],
        'Percentage': Social_1a_this_month['Formatted Total Percentage'],
        'Cumulative Number': Social_1a_this_month['Cumulative Number'],
        'Cumulative Percentage': Social_1a_this_month['Formatted Cumulative Percentage']
    })
    
    Social_tables = {
        'Social_remediation_table' : Social_remediation_table
    }

    Social_headline_dict = {
        'Social_life_critical_total_no': format(Social_1a_this_month.iloc[5, 5], ','),
        'Social_life_critical_total_change': Change_line_in_DR(Social_1a_this_month.iloc[5, 5] - Social_1a_last_month.iloc[5, 5]),

        'Social_started_no': format(Social_1a_this_month.loc[2, 'Cumulative Number'], ','),
        'Social_started_pct': Social_1a_this_month.loc[2, 'Formatted Cumulative Percentage'],
        'Social_started_change': Change_line_in_DR(Social_1a_this_month.loc[2, 'Cumulative Number'] - Social_1a_last_month.loc[2, 'Cumulative Number']),

        'Social_completed_no': format(Social_1a_this_month.loc[1, 'Cumulative Number'], ','),
        'Social_completed_pct': Social_1a_this_month.loc[1, 'Formatted Cumulative Percentage'],
        'Social_completed_change': Change_line_in_DR(Social_1a_this_month.loc[1, 'Cumulative Number'] - Social_1a_last_month.loc[1, 'Cumulative Number']),
    }
    

    Social_section_dict = {
        'Social_RP_surveyed' : Social_misc.loc[0, 'Number'],
        'Social_RP_excluded' : Social_misc.loc[1, 'Number'],

        'Social_life_critical_total_no': format(Social_1a_this_month.loc[5, 'Total Number'], ','),
        'Social_life_critical_total_change': Change_line_in_DR(Social_1a_this_month.loc[5, 'Total Number'] - Social_1a_last_month.loc[5, 'Total Number']),

        'Social_recent_assessment_total' : format(Social_1c_this_month.loc[5, 'Total Number'], ','),
        'Social_recent_assessment_remediated' : format(Social_1b_this_month.loc[0, 'Total Number'], ','),

        'Social_crossover_total' : format(Social_misc.loc[2, 'Number']),

        'Social_started_no': format(Social_1a_this_month.loc[1, 'Cumulative Number'], ','),
        'Social_started_pct': Social_1a_this_month.loc[2, 'Formatted Cumulative Percentage'],
        'Social_started_change': Change_line_in_DR(Social_1a_this_month.loc[1, 'Cumulative Number'] - Social_1a_last_month.loc[1, 'Cumulative Number']),

        'Social_bc_signoff_no' : format(Social_1a_this_month.loc[0, 'Total Number'], ','),
        'Social_bc_signoff_pct' : Social_1a_this_month.loc[0, 'Formatted Cumulative Percentage'],
        'Social_bc_signoff_change' : Change_line_in_DR(Social_1a_this_month.loc[1, 'Total Number'] - Social_1a_last_month.loc[1, 'Total Number']),

        'Social_completed_no': format(Social_1a_this_month.loc[1, 'Cumulative Number'], ','),
        'Social_completed_pct': Social_1a_this_month.loc[1, 'Formatted Cumulative Percentage'],
        'Social_completed_change': Change_line_in_DR(Social_1a_this_month.loc[1, 'Cumulative Number'] - Social_1a_last_month.loc[1, 'Cumulative Number']),

        'Social_not_started_no' : format(Social_1a_this_month.loc[3, 'Total Number'] + Social_1a_this_month.loc[4, 'Total Number'], ','),
        'Social_not_started_pct' : format_percentage(Social_1a_this_month.loc[4, 'Total Percentage'] + Social_1a_this_month.loc[3, 'Total Percentage']),
        'Social_not_started_change' : Change_line_in_DR((Social_1a_this_month.loc[3, 'Total Number'] + Social_1a_this_month.loc[4, 'Total Number']) - (Social_1a_last_month.loc[3, 'Total Number'] + Social_1a_last_month.loc[4, 'Total Number'])),

        'Social_plans_no' : format(Social_1a_this_month.loc[3, 'Total Number'], ','),
        'Social_plans_pct' : Social_1a_this_month.loc[3, 'Formatted Total Percentage'],
        'Social_plans_change' : Change_line_in_DR(Social_1a_this_month.loc[3, 'Total Number'] - Social_1a_last_month.loc[3, 'Total Number']),

        'Social_unique_no' : format(Social_misc.loc[3, 'Number'], ','),

        'Social_18m_starts_pct' : Social_1a_this_month.loc[2, 'Cumulative 18m Percentage'],
        'Social_11m_starts_pct' : Social_1a_this_month.loc[2, 'Cumulative 11_18m Percentage'],

        'Social_rp_total' : format(Social_1b_this_month.loc[5, 'Total Number'], ','),
        'Social_rp_change' : Change_line_in_DR(Social_1b_this_month.loc[5, 'Total Number'] - Social_1b_last_month.loc[5, 'Total Number']),

        'Social_rp_prior_completes_no' : format(Social_1b_this_month.loc[0, 'Total Number'], ','),
        'Social_rp_identified_no' : format(Social_1b_this_month.loc[5, 'Total Number'] - Social_1b_this_month.loc[0, 'Total Number'], ','),

        'Social_rp_completes_no' : format(Social_1b_this_month.loc[1, 'Cumulative Number'], ','),
        'Social_rp_completes_pct' : Social_1b_this_month.loc[1, 'Formatted Cumulative Percentage'],
        'Social_rp_completes_change' : Change_line_in_DR(Social_1b_this_month.loc[1, 'Cumulative Number'] - Social_1b_last_quarter.loc[1, 'Cumulative Number']),

        'Social_rp_starts_no' : format(Social_1b_this_month.loc[2, 'Cumulative Number'], ','),
        'Social_rp_starts_pct' : Social_1b_this_month.loc[2, 'Formatted Cumulative Percentage'],
        'Social_rp_starts_change' : Change_line_in_DR(Social_1b_this_month.loc[2, 'Cumulative Number'] - Social_1b_last_quarter.loc[2, 'Cumulative Number']),

        'Social_rp_plans_no' : format(Social_1b_this_month.loc[3, 'Total Number'], ','),
        'Social_rp_plans_pct' : Social_1b_this_month.loc[3, 'Formatted Total Percentage'],
        'Social_rp_plans_change' : Change_line_in_DR(Social_1b_this_month.loc[3, 'Total Number'] - Social_1b_last_quarter.loc[3, 'Total Number'])
    }
    return Social_tables, Social_headline_dict, Social_section_dict
