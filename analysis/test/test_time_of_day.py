""" testing chisquare from time_of_day """

import pandas as pd
import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
from analysis import time_of_day

def test_chisquare():
    
    test = pd.DataFrame()
    test.insert(0, '1', [1,2,3])
    test.insert(1, '2', [4,5,6])
    
    pval, contributions = time_of_day.chisquare(test, ['1', '2'], plot_expected = False)
    assert contributions.shape == test.shape