'''
Dataframe managing module ()
Created by Junho Kim
Latest edit : Mar 01 2023
'''
import pandas as pd

def insert(dtfr : pd.core.frame.DataFrame, location : int, in_value : list):
    '''Insert Value in row. Empty Value will be filled with NaN'''
    dtfr.loc[location + 0.5] = in_value
    return dtfr

def length_match(og_list : list, df_length: int):
    gap = df_length - len(og_list)
    if gap > 0:
        return og_list.append(None * gap)
    elif gap < 0:
        return 'Err_df_001'
    else:
        return og_list
    
