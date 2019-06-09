#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:57:21 2019

@author: prawigya
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import statsmodels.formula.api as sm
filename = '50_Startups.csv'
data = pd.read_csv(filename)
X = data.iloc[:,:-1].values
Y = data.iloc[:,4].values

le = LabelEncoder()
X[:,3] = le.fit_transform(X[:,3])
oe = OneHotEncoder(categorical_features=[3])
X = oe.fit_transform(X).toarray()
X = X[:,1:]

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(y_pred)
print()
print()
print(model.score(x_test, y_test))
##
##
X = np.append(arr=np.ones([50,1]).astype(int), values=X, axis=1) 
print(X)
print("Break")
print(X.shape)
x_opt = X[:,[0,1,2,3,4,5]]
print("Break X_opt")
print(x_opt.shape)
#print(x_opt)
regg_OLS = sm.OLS(endog=Y, exog=x_opt).fit()
print(regg_OLS.summary())

x_opt = X[:,[0,1,3,5]]
print("Break X_opt2")
print(x_opt.shape)
print(x_opt)
regg_OLS = sm.OLS(endog=Y, exog = x_opt).fit()
print(regg_OLS.summary())
x1_train, x1_test, y1_train, y1_test = train_test_split(x_opt, Y, test_size = 0.2, random_state=0)
m= LinearRegression()
m.fit(x1_train, y1_train)
print(m.score(x1_test, y1_test))
