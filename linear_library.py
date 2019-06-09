#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:06:02 2019

@author: prawigya
"""

import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn import linear_model
#data = [[100],[200],[300],[400]]
data = [100,200,300,400]
feature = [[100],[200],[300],[400]]


labels = [500, 1100, 1700, 2300]

c, p = pearsonr(data, labels)
print("r=",c)

plt.scatter(feature, labels, c='red')
plt.xlabel("Monthly units")
plt.ylabel("Price")

clf = linear_model.LinearRegression()
clf = clf.fit(feature, labels)
result = clf.predict([[160],[380]])
plt.plot([[160],[380]],result, c='blue')

