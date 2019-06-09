#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:35:27 2019

@author: abhishek
"""

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.linear_model import LinearRegression
import pandas as pa
from sklearn.model_selection import train_test_split
import numpy as np
data=pa.read_csv("data2.csv").values
X=data[:,:-1]
Y=data[:,4]
print(X,Y)
le=LabelEncoder()
X[:,0]=le.fit_transform(X[:,0])
print(X)
oh=OneHotEncoder(categorical_features=[0])
X=oh.fit_transform(X).toarray()
print(X)
X=X[:,1:]
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.2,random_state=7)
model=LinearRegression()
model.fit(x_train,y_train)
print(model.predict(x_test))
print(y_test)
result=model.score(x_train,y_train)
print(result)

#new data
new_data=np.array([['Development',1596,1,4.0],['Testing',1256,2,4.1],['UX Designer',1489,3,4.5]])
new_data[:,0]=le.fit_transform(new_data[:,0])
new_data=oh.fit_transform(new_data).toarray()
new_data=new_data[:,1:]
print("New Data prediction: ", model.predict(new_data))
