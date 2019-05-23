#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:07:22 2019

@author: prawigya
"""

#Sample file
import pandas as pa
file = "sample.xls"
data = pa.read_excel(file)
print(data)

#Getting all the columns
print(data.columns)

#printing head and tail
print(data.head())
print(data.tail())

#Finding out category wise sale
sdata = data.groupby('Category').sum()
print(sdata['Sales'])
"""
Output will be like

Furniture   75645352
Office Supplies 7898213
Technology      8234234

"""

#Join, merge, group by, concatenate
