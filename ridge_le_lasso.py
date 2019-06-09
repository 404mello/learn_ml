#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:22:00 2019

@author: prawigya
"""

from mglearn.datasets import load_extended_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

X, y = load_extended_boston()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
lr = LinearRegression().fit(x_train, y_train)
print("Accuracy of train data: ", lr.score(x_train, y_train))
print("Accuracy of test data: ", lr.score(x_test, y_test
lasso1 = Lasso(alpha = 0.1).fit(x_train, y_train)
print("Training score ", lasso1.score(x_train, y_train))
print("Test score ", lasso1.score(x_test, y_tetst))


