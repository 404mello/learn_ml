#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:32:25 2019

@author: prawigya
"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housedata = load_boston()
X = housedata.data
Y = housedata.target
#print(X, Y)

#Getting description of dataset
#print(housedata.DESCR)

#Getting feature names from dataset
#print(housedata.feature_names)

df = pd.DataFrame(data = X, columns = housedata.feature_names)
sns.heatmap(df.corr(), annot = True)
plt.show()
sns.distplot(Y, bins = 50)
plt.show()

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2 ,random_state = 2)
model = LinearRegression()
model.fit(x_train, y_train)
#print(model.predict(x_test))
#print(sum(model.predict(x_test)-y_test))
print("Accuracy")
variance = model.score(x_test, y_test)
print(variance)

#Plot the scatter plot
plt.scatter(model.predict(x_test), model.predict(x_test)-y_test, s=10, c='blue', label = "Test Data")

plt.scatter(model.predict(x_train), model.predict(x_train)-y_train, s=10, c='red', label = "Train Data")

plt.hlines(y=0, xmin=0, xmax=50, linewidth=2)
plt.title("My Second Demo of ML")
plt.legend()
plt.show()
