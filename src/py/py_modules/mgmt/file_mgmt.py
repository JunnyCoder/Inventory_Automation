'''
Created by Junho Kim
Latest edit : Mar 01 2023

'''
import os

def file_check(file_name):
    '''Check whether the file is existing'''
    if os.path.isfile(file_name):
        return True
    else:
        return False

def file_delete(file_name):
    '''File delete'''
    if file_check(file_name):
        os.remove(file_name)
    else:
        return 'Err_file_001'
