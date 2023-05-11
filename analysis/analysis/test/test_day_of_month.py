""" testing find_mean from day_of_month """

import pandas as pd
import numpy as np
from analysis import day_of_month

def test_find_mean():
    test_df = pd.DataFrame()
    test_df.insert(0, '1', [1,1,1,1,1])
    test_df.insert(1, '2', [2,2,2,2,2])
    
    by_row = day_of_month.find_mean(test_df)
    assert by_row.iloc[0] == 1
    
    by_col = day_of_month.find_mean(test_df, by_row = False)
    assert by_col.iloc[0] == 1
    
