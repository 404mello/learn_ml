#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 11:22:23 2019

@author: prawigya
"""

#Normalization
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
import numpy as np

data = [[16,12],[16,18],[32,16],[32,8],[16,16]]

#Scaling
norm = MinMaxScaler(feature_range=(0,1))
scaledata = norm.fit_transform(data)
np.set_printoptions(precision=3)
print(scaledata)

#Standardization
print("Standardization")
norm = StandardScaler().fit(data)
scaledata = norm.transform(data)
print(scaledata)

#Normalizer
norm = Normalizer().fit(data)
scaledata = norm.transform(data)
print(scaledata)

#Binarizer
norm = Binarizer(threshold=1).fit(data)
scaledata = norm.transform(data)
print(scaledata)

#X=data[:,0:8]
#Y=data[;,8]

#Setting precision to data



