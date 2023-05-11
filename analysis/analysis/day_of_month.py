import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def find_mean(df, by_row = True):
    '''Returns the mean of a dataframe across either rows or columns;
        If by_row = True, return mean across rows, else across columns
        
        Inputs:
        
        df (DataFrame): DataFrame containing original data
        by_row (boolean): Determines if mean is taken across rows or across columns
        
        Outputs:
        
        no_totals (DataFrame): DataFrame with mean across desired dimension
    '''
    no_totals = df.iloc[:-1, :-1] # get rid of totals
    if by_row: 
        return no_totals.mean(axis = 1)
    else: 
        return no_totals.mean(axis = 0)