#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 18:58:58 2019

@author: prawigya
"""

import pandas as pd
import numpy as np
filename = 'winequality-red.csv'
df = pd.read_csv(filename)
print(df.head())
names = list(df.columns)
print(names)