'''
Author: Matthew Bandura
Created on Thursday 20th November, 14:12:17  
'''

import pandas as pd

def generate_social_misc():
    #UPDATE QUARTERLY FROM FELICIA
    social_respondant_rps = 549
    social_excluded_rps = 939

    #UPDATE MONTHLY FROM FELICIA
    social_in_other_programmes = 148

    #UPDATE MONTHLY FROM FILTERING PORTFOLIO LIST
    social_not_in_other_programmes = 1165

    social_misc= pd.DataFrame({ 'Number': [social_respondant_rps, social_excluded_rps, social_in_other_programmes, social_not_in_other_programmes]}, index = ['Respondant RPs', 'Excluded RPs', 'In other programmes', 'Not in other programmes'])
    print(social_misc)
    return social_misc

    