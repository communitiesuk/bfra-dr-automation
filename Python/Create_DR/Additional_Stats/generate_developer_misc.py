'''
Author: Matthew Bandura
Created on Thursday 20th November, 13:57:27  
'''


import pandas as pd

def generate_developer_misc():
    #UPDATE QUARTERLY FROM RYAN
    dev_total_dwellings = 148000
    dev_started_completed_dwellings = 69000
    dev_expected_starts = 559
    dev_expected_completes = 347

    developer_misc= pd.DataFrame({ 'Current Month': [dev_total_dwellings, dev_started_completed_dwellings, dev_expected_starts, dev_expected_completes]}, index = ['Total number of dwellings', 'Started and completed number of dwellings', 'Expected starts', 'Expected completes'])
    print(developer_misc)
    return developer_misc