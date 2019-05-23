#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:58:56 2019

@author: prawigya
"""

#This script works on the automobile dataset
#Source of the assignment : https://pynative.com/python-pandas-exercise/

import pandas as pd
#Reading the dataset 
df = pd.read_csv('Automobile_data.csv')


#Question1 : From given data set print first and last five rows
print(df.head())
print()
print(df.tail())



#Question2: Clean data and update the CSV file
#ToDo: Replace all column values which contain ‘?’ and n.a with NaN.

df = pd.read_csv("Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})

#df.to_csv('Automobile_data_clean.csv')


#Question3: Find the most expensive car company name
print(df.columns)
print("The maximum priced car is: ")
print(df[['company','price']][df['price']==df['price'].max()])
#PQuestion4: Print All Toyota Cars details

#Question5: Count total cars per company

#Question6: Find each company’s Higesht price car

#Question7: Find the average mileage of each car making company

#Question8: Sort all cars by Price column

#Question9: Concatenate two data frames using following conditions