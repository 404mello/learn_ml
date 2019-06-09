#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:27:25 2019

@author: prawigya
"""

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
array = ['A','B','C','A','B','C','A','B','C','A','B','C']
le = LabelEncoder()
oe = OneHotEncoder()
le = le.fit_transform(array)
oe = oe.fit_transform([le]).toarray()
data = pd.read_csv('data2.csv').values
X = data[:,:-1]
Y = data[:,4]
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])
#print(X)
oh = OneHotEncoder(categorical_features=[0])
X = oh.fit_transform(X).toarray()
#print(X)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=8)
model = LinearRegression()
model.fit(x_train, y_train)
result = model.score(x_test, y_test)*100
print(result)
X = X[:,1:]


#Using sample data
"""
new_data = np.array([['Testing',2100,1,1.13], ['Development', 2104, 2, 1.5], ['UX Designer', 2300, 0, 1.1]])
new_data[:,0] = le.fit_transform(new_data[:,0])
new_data = oh.fit_transform(new_data).toarray()
new_data = new_data[:,1:]
"""