#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:42:48 2019

@author: prawigya
"""

from sklearn.metrics import classification_report, confusion_matrix
od = [1,0,1,0,2] #Original data
pd = [0,1,1,0,2] #Predicted data
print("Confusion matrix")
print(confusion_matrix(od, pd))
print("Classification report")
print(classification_report(od, pd))

