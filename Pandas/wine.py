#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:30:06 2019

@author: prawigya
"""

#This script reads the csv file wine_quality.csv and analyses/ visualises it.
import pandas as pd
df = pd.read_csv('winequality-red.csv')
cols = df.columns
print(list(cols))