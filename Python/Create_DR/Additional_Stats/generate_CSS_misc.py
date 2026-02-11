import pandas as pd
import openpyxl
'''
Author: Matthew Bandura
Created on Thursday 20th November, 12:12:18
'''


def generate_CSS_misc(CSS_data_path):

    #UPDATE MONTHLY BY FILTERING PORTFOLIO LIST
    CSS_transfers_this_month = 229
    CSS_transfers_last_month = 228
 
    #UPDATE MONTHLY FROM HOMES ENGLAND
    CSS_GFA_this_month = 980
    CSS_GFA_last_month = 944

    CSS_wb = openpyxl.load_workbook(CSS_data_path, read_only= True, data_only= True)
    CSS_misc_stats = CSS_wb['Misc Stats']
    #AUTO UPDATE
    CSS_social = CSS_misc_stats['A2'].value
    CSS_private = CSS_misc_stats['B2'].value


    CSS_misc= pd.DataFrame({ 'Current Month': [CSS_GFA_this_month, CSS_transfers_this_month, CSS_social, CSS_private], 'Last Month': [CSS_GFA_last_month, CSS_transfers_last_month, '', '']}, index = ['CSS Transfers', 'GFA', 'Social Tenure', 'Private Tenure'])
    return CSS_misc