#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:15:08 2019

@author: prawigya
"""

from sklearn.svm import SVC
import matplotlib.pyplot as plt
from scipy.misc import imread, bytescale, imresize
from sklearn.datasets import load_digits

digits = load_digits()
x, y = digits.data, digits.target
print(x.dtype)
print(x.max())
print(x.min())
print(x.shape)

clf = SVC(gamma = 0.1)
clf.fit(x, y)
img = imread('digit3.png')
img = imresize(img, (8,8))
print(img)

img = img.astype(x.dtype)
img = bytescale(img, high = 16.0, low = 0)
new_testdata = []
for r in img:
    for c in r:
        new_testdata.append(sum(c)/3.0)
print(new_testdata)
p = clf.predict([new_testdata])
print(p)