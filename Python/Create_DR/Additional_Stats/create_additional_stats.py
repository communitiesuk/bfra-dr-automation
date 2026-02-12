'''
Author: Matthew Bandura
Created on Thursday 23rd October, 11:26:25
'''
import pandas as pd
from generate_filepaths import generate_filepaths
from generate_ACM_start_trajectory import generate_ACM_start_trajectory
from generate_BSF_reg_status import generate_BSF_reg_status
from generate_BSF_misc import generate_BSF_misc
from generate_CSS_misc import generate_CSS_misc
from generate_developer_misc import generate_developer_misc



def create_AdditionalStats():
    Master_analytical, BSF_cut, last_month_BSF_cut, CSS_data_path, month = generate_filepaths()
    #FULLY AUTOMATED
    ACM_start_trajectory = generate_ACM_start_trajectory(Master_analytical)

    BSF_reg_status = generate_BSF_reg_status(BSF_cut, last_month_BSF_cut)
    
    BSF_misc = generate_BSF_misc(BSF_cut)

    #UPDATE MONTHLY
    CSS_misc = generate_CSS_misc(CSS_data_path)

    #UPDATE QUARTERLY
    Developer_misc = generate_developer_misc()

    #save the additional stats
    with pd.ExcelWriter(f'Q:\\BSP\Automation\\DR Automation\\Excel_inputs\\[PUT ADDITIONAL DR STATS HERE]\\[AUTOMATION]\\Additional_stats_{month}.xlsx') as writer:
        ACM_start_trajectory.to_excel(writer, sheet_name = 'ACM_start_trajectory', index = False)
        BSF_reg_status.to_excel(writer, sheet_name = 'BSF_reg_status', index = False)
        BSF_misc.to_excel(writer, sheet_name = 'BSF_misc')
        CSS_misc.to_excel(writer, sheet_name = 'CSS_misc')
        Developer_misc.to_excel(writer, sheet_name = 'Developer_misc')
        


create_AdditionalStats()
