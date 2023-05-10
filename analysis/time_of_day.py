""" Functions for time of day analysis """

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

def chisquare(df, cols, plot_expected=True):
    """ Compare distribution of crash numbers between columns. 
        
        Inputs: 
        
        df (DataFrame): dataframe containing our sample data
        cols (list): list of columns we want to feed into function
        plot_expected (boolean): if we want to plot the contingency plot 
        
        Outputs:
        pval (float): p-value for our calculated statistic
        contributions (DataFrame): shows contributions to test statistic from each cell
    
    """
    assert len(cols) >= 2
    for c in cols:
        assert c in df.columns, f"{c} is not a column in DataFrame (must be one of {df.columns})"
    contingency = df.loc[:, cols]
    chi2, pval, dof, expected = st.chi2_contingency(contingency)

    if plot_expected:
        plt.plot(expected,
                 label=[f'Expected {col}' for col in cols],
                 linestyle='--')
        plt.plot(contingency,
                 label=contingency.columns)
        plt.legend()
        plt.show()

    # contributions table for each cell in the contingency table
    contributions = (contingency - expected)**2 / expected
    return pval, contributions