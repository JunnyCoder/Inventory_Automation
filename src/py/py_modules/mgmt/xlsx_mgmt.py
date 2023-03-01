'''
Created by Junho Kim
Latest edit : Mar 01 2023
'''
import os
import pandas as pd

def excel_mgmt_master(file_name, mgmt_type, cols_dic=None, sheet_number=0, header=1, index=0):
    '''Excel manager master(No delete, only create, read, edit)'''
    if excel_file_check(file_name):   # Check if the file exists in the folder
        df = pd.read_excel(file_name, sheet_number, header=header, index_col=index)
        if mgmt_type == 'read':
            return df
        elif mgmt_type == 'edit':

            # Update function is needed here

            return True
        else:
            return 'Err_Invalid_Mode'

    elif mgmt_type == 'write':
        if cols_dic is not None and isinstance(cols_dic, pd.core.frame.DataFrame):
            cols_dic.reset_index(drop=True)
            cols_dic.to_excel(file_name, index=False)
            return cols_dic
        elif cols_dic is not None and isinstance(cols_dic, dict):
            df = pd.DataFrame(cols_dic, index=None)
            df.to_excel(file_name, index=False)
            # print('File created successfully.')
            return df
        elif cols_dic is not None and isinstance(cols_dic, list):
            df = pd.DataFrame(columns=cols_dic, index=None)
            df.to_excel(file_name, index=False)
            # print('File with only Column created successfully.')
            return df
        elif cols_dic is None:
            return 'Err_Empty_Cols_Data'
        else:
            return 'Err_Wrong_Data_type'

    else:
        return 'Err_File_Not_Exist'



def excel_file_check(file_name):
    '''Check is the excel file is existing'''
    if os.path.isfile(file_name):
        return True
    else:
        return False


# dataframe works
def excel_cell_mgmt(df, cell, work, sheet_number=0, header=1, index=0):
    '''Manage cell '''
    return True

def excel_row_mgmt(df, row, work, sheet_number=0, header=1, index=0):
    return True

def excel_column_mgmt(df, row, work, sheet_number=0, header=1, index=0):
    return True

def excel_sheet_mgmt(df, row, work, sheet_number=0, header=1, index=0):
    return True

def excel_file_mgmt(df, row, work, sheet_number=0, header=1, index=0):
    return True



def excel_del_mgmt(del_data_type, is_super = False):
    '''Excel delete managing function. (Cell, Row, Column, Sheet, File)'''
    if is_super :
        print("can delete"+str(del_data_type))
    else:
        return False
