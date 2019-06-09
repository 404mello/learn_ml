#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:28:30 2019

@author: prawigya
"""

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import confusion_matrix, classification_report

filename= 'diabetes.csv'
df = pd.read_csv(filename)
#print(df.head)
array = df.values
X = array[:,0:-1]
y = array[:,-1]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy of train data")
print(model.score(x_train, y_train))
print("Accuracy of test data")
print(model.score(x_test, y_test))
print("Confusion Matrix")
print(confusion_matrix(y_test, y_pred))
print("Classifiation Report")
print(classification_report(y_test, y_pred))