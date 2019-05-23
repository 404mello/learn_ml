#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:45:45 2019

@author: prawigya
"""
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
filename = "winequality-red.csv"
data = read_csv(filename)
names = list(data.columns)
scatter_matrix(data)
plt.show()

print("Scatter plot")