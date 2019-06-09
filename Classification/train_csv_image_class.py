#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:35:08 2019

@author: prawigya
"""

import pandas as pd
from sklearn.svm import SVC
from scipy.misc import bytescale, imread, imresize

df = pd.read_csv('train.csv')
print(df.head())
array = df.values
Y = array[:,0]
X = array[:,1:]
print(X.shape)
print(X.max())
print(X.min())

clf = SVC(gamma = 0.1)
clf.fit(X, Y)

img = imread('digit3.png')
img = imresize(img, (8,8))
print(img)

img = img.astype(X.dtype)
img = bytescale(img, high = X.max(), low = X.min())
new_testdata = []

for r in img:
    for c in r:
        new_testdata.append(sum(c)/3.0)

p = clf.predict([new_testdata])
print(p)