#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:36:02 2019

@author: prawigya
"""

import pandas as pd
df = pd.read_csv('iris.csv')
print("Iris dataset")

#print("Checking for any duplicate data in the iris dataset")
if(True in list(df.duplicated())):
    print("Duplicates exist in the dataset")
else:
    print("No duplicates in the dataset")

