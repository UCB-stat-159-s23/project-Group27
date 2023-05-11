""" Functions for time of day analysis """

import matplotlib.pyplot as plt
import scipy.stats as st
import matplotlib.cm as cm

def chisquare(df, cols, plot_expected=True):
    """ Compare distribution of crash numbers between columns.

        Inputs:

        df (DataFrame): dataframe containing our sample data
        cols (list): list of columns we want to feed into function
        plot_expected (boolean): if we want to plot the contingency plot

        Outputs:
        pval (float): p-value for our calculated statistic
        contributions (DataFrame): contributions to test statistic from each cell

    """
    assert len(cols) >= 2
    for c in cols:
        assert c in df.columns, f"{c} is not a column in DataFrame (must be one of {df.columns})"
    contingency = df.loc[:, cols]
    chi2, pval, dof, expected = st.chi2_contingency(contingency)

    if plot_expected:
        colors = cm.tab10.colors
        for i in range(len(cols)):
            color = colors[i]
            exp = expected[:, i]
            obs = contingency.iloc[:, i]
            label = contingency.columns[i]

            plt.plot(exp,
                     label=f'Expected {label}',
                     linestyle='--',
                     c=color)
            plt.plot(obs,
                     label=label,
                     c=color)

        plt.legend()
        plt.show()

    # contributions table for each cell in the contingency table
    contributions = (contingency - expected)**2 / expected
    return pval, contributions