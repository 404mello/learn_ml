#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:09:07 2019

@author: prawigya
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.preprocessing import StandardScaler

filename = 'crop_yeild.csv'
df = pd.read_csv(filename)
le = LabelEncoder()
print(list(df.columns))


"""
#Standardizing
data = [[16,12],[16,18],[32,16],[32,8],[16,16]]
norm = StandardScaler().fit(data)
scaledata = norm.transform(data)
print(scaledata)
"""

X = df.iloc[:,:-1].values
features = X

norm = StandardScaler().fit(X[:,2:4])
scaledata - norm.transform(X[:,2:4])


Y = df.iloc[:,-1].values
X[:,1] = le.fit_transform(X[:,1])
print("After LE", X.shape)
X[:,0] = le.fit_transform(X[:,0])
#oe = OneHotEncoder()
oe = OneHotEncoder(categorical_features=[0,1])
X = oe.fit_transform(X).toarray()
print("After OE", X.shape)
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size = 0.2, random_state = 0)
model = LinearRegression()
model.fit(x_train,y_train)
print("Accuraccy=",model.score(x_test, y_test)*100)
#X = np.append(arr = np.ones([49,1]).astype(int), values=X, axis=1)


