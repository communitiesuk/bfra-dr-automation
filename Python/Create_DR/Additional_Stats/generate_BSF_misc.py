'''
Author: Matthew Bandura
Created on Wednesday 19th November, 13:49:37
'''



import pandas as pd
import openpyxl


def generate_BSF_misc(BSF_cut):

    #open the BSF cut in read only so it doesn't hang infinitely
    BSF_wb = openpyxl.load_workbook(BSF_cut, read_only= True, data_only= True)

    BSF_tables_DR = BSF_wb['Essential Tables for DR']
    BSF_RAS_tables = BSF_wb['RAS Tables']

    #get the values from the relevant cells
    BSF_reimburse = BSF_RAS_tables['C15'].value
    BSF_transfers_expected = BSF_RAS_tables['C16'].value
    BSF_transfers_actual = BSF_RAS_tables['C19'].value
    
    BSF_dwellings_total = BSF_tables_DR['D40'].value
    BSF_FRAEW = BSF_tables_DR['C44'].value
    BSF_CAN = BSF_tables_DR['D44'].value

    BSF_misc = pd.DataFrame({ 'Number' : [BSF_transfers_actual, BSF_reimburse, BSF_transfers_expected, BSF_dwellings_total, BSF_FRAEW, BSF_CAN]}, 
                            index = [ 'Developer transfers: Actual','Developer transfers: Anticipated', 'Developer transfers: Reimburse', 'Dwellings', 'FRAEW', 'CAN'])


    BSF_wb.close()
    return BSF_misc
