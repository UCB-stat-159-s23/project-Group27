# A Study of California Motor Vehicle Traffic Collisions

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-Group27/main?labpath=main.ipynb)

Contributors: Jeffrey Fan, Leah Hong, Janise Liang, and Nick Melamed (Group 27)

# Background and Motivation

Motor vehicle crashes are unfortunately quite prevalent in the state of California. We were interested in determining whether or not there was a seasonality effect on car crashes based on differing periods of time (time of day, day of month, and month of year). If seasonality patterns emerged, such information could be used to inform policy-decisions (i.e., if nighttime crashes were more common, increasing nighttime driver safety on highways could be one such intervention). 

We utilized various statistical methods, including a Chi-Square test and Kruskal-Wallis test, to make our determinations. 

# Data
Data is sourced from https://www.chp.ca.gov/programs-services/services-information/switrs-internet-statewide-integrated-traffic-records-system/switrs-2019-report. The data set was created from the Microsoft Excel spreadsheets for the different sections selected. 

# Analysis

- `main.ipynb` : main narrative notebook that summarizes all the results
- `analysis/by_county.ipynb` : notebook that explores total crashes based on each county in 2019
- `analysis/day_of_month.ipynb` : notebook that explores total crashes based on the day of a month or month in a year
- `analysis/time_of_day.ipynb` : notebook that explores fatal and injury crashes based on the time of day

# Installation

Run `make env` in your terminal/shell to set up the conda environment.

Then use resulting `traffic-collisions` kernel to run all analysis notebooks.

# Testing

To test the `analysis functions`, navigate to the root directory and run `pytest`.

# License

This project is released under the terms of the MIT License.
