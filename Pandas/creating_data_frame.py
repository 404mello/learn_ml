#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 23:08:15 2019

@author: prawigya
"""

import pandas as pd
import random
print("Hello")
#Defining the features
features = ['consciousness_level', 'blood_alc_level', 'accident_rate', 'speed']
l_cl = [random.randint(1,10) for i in range(100)]
l_bal = [random.randint(1,100) for i in range(100)]
l_ar = [random.randint(1,100) for i in range(100)]
l_speed = [random.randint(40,180) for i in range(100)]

#Creating a dataframe
df = pd.DataFrame([l_cl, l_bal, l_ar, l_speed], index=features)

#Getting the transpose of the dataframe created
df = df.T

#Adding a label
label = ['Yes','No']
accident = [label[random.randint(0,1)] for i in range(100)]

#Adding the column to the dataframe
df['accident']=accident

#Saving the dataframe to a CSV
df.to_csv('sample_accident_random_data.csv')