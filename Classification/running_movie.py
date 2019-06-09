#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 13:08:53 2019

@author: prawigya
"""

import movie
datasets, labels = movie.CreateDataset()
print(datasets, labels)
predict = [[1,1]]
result = movie.classify(predict, datasets, labels, 3)
print(predict)
print(result)