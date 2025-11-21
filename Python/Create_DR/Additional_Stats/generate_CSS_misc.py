import pandas as pd
'''
Author: Matthew Bandura
Created on Thursday 20th November, 12:12:18
'''


def generate_CSS_misc():

    #UPDATE MONTHLY BY FILTERING PORTFOLIO LIST
    CSS_transfers_this_month = 228
    CSS_transfers_last_month = 170
 
    #UPDATE MONTHLY FROM HOLLY
    CSS_GFA_this_month = 820
    CSS_GFA_last_month = 820


    CSS_misc= pd.DataFrame({ 'Current Month': [CSS_transfers_this_month, CSS_GFA_this_month], 'Last Month': [CSS_transfers_last_month, CSS_GFA_last_month]}, index = ['CSS Transfers', 'GFA'])
    return CSS_misc