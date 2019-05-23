#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:37:18 2019

@author: prawigya
"""
import pandas as pa
data1 = {'Name':['A','B','C'], 'Marks':[80,90,100], 'Grade': ['C','B','A']}
df1 = pa.DataFrame(data1)
data2 = {'Name':['E','F','G'], 'Marks':[70,40,30], 'Grade': ['C','F','F']}
df2 = pa.DataFrame(data2)
print(df1)
print()
print(df2)
print()
concatData = pa.concat([df1,df2], axis=0)
print(concatData)

print()

concatData2 = pa.concat([df1,df2], axis=1)
print(concatData2)

print()
#On basis of keys
concatData3 = pa.concat([df1,df2], keys = ['A','B'])
print(concatData3)

print()
#We can use append also
print(df1.append(df2))