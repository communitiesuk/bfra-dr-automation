# '''
# Author: Matthew Bandura
# Created on Wednesday 4th January, 13:26:17  
# '''

# import pandas as pd
# import openpyxl

# def generate_social_misc(MI_tables, month, year, last_month):

#     month_year = month[:3] + '-' + str(year)[2:] +'1'

#     #UPDATE AUTOMATICALLY
#     MI_wb = openpyxl.load_workbook(MI_tables)
#     Combined_2 = MI_wb['Combined_2']

#     remediation_unknown = Combined_2['F17'].value
#     eligibility_pending_current = round(Combined_2['F18'].value, -2)

#     social_current = pd.DataFrame({f'{month_year}': [remediation_unknown, eligibility_pending_current], 'Number' : ['Remediation progress currently unknown', 'Social sector - Eligibility pending ']})

#     social_misc = pd.read_excel(f'Q:\\BSP\Automation\\DR Automation\\Excel_inputs\\[PUT ADDITIONAL DR STATS HERE]\\[AUTOMATION]\\Additional_stats_{month}.xlsx', sheet_name = 'Social_misc')

    
#     social_misc = social_misc.set_index('Number')

#     social_current = social_current.set_index('Number')
#     social_misc = social_misc.join(social_current, how='outer')
#     social_misc = social_misc.reset_index()


#     MI_wb.close()

#     return social_misc

    