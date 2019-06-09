#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:59:04 2019

@author: prawigya
"""

from scipy.stats import pearsonr
X = [4,3,1,8,9]
Y = [1,3,4,8,7]

corr, p = pearsonr(X,Y)
print(corr)