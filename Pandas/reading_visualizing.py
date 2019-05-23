#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:38:58 2019

@author: prawigya
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
#Reading data frame
df = pd.read_csv('sample_accident_random_data.csv')
cols = df.columns

#Extracting the consciousness data into list
cons = list(df['consciousness_level'])
#Extracting the blood alcohol level data into list
bal = list(df['blood_alc_level'])

#Correlation between consciousness level and bal
matplotlib.style.use('ggplot')
plt.scatter(cons, bal)
corr = np.corrcoef(bal, cons)
print("The correlation between consciousness_level and blood_alcohol_level is ")
print(corr)