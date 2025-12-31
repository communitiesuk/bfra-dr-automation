'''
Author: Matthew Bandura
Created on Monday 17th November, 14:51:24
'''


import pandas as pd
def generate_ACM_start_trajectory(Master_analytical):
    #access the start trajectory sheet in the master analytic
    ACM_start_trajectory = pd.read_excel(Master_analytical, sheet_name = 'Start_Trajectory', index_col= None)
    #remove the time that python adds to the dates
    ACM_start_trajectory['StartedDatePlanned'] = ACM_start_trajectory['StartedDatePlanned'].dt.date

    #rename the cols to be consistent with how additional stats is currently generated
    ACM_start_trajectory.rename(columns={ACM_start_trajectory.columns[-4]: 'Enforcement previous', ACM_start_trajectory.columns[-3]: 'JIT previous'}, inplace=True)

    
    return ACM_start_trajectory
