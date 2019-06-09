#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 12:15:39 2019

@author: prawigya
"""

from pandas import read_csv
from sklearn.decomposition import PCA
#load data
filename = 'diabetes.csv'
#names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = read_csv(filename)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

#Feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

#Summarize components
print("Explained Variance: %s",fit.explained_variance_ratio_)
print(fit.components_)

