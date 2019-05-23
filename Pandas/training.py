#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:51:57 2019

@author: prawigya
"""

#Types of datas in pandas: series and data frames.
#Data series works with 1D array
#Data frame works with 2D array
#Can load data from any sources: excel, csv, html, etc.
#Easy to manipulate, remove duplicates etc.
import pandas as pa

#Series
print("Series")
s = pa.Series([1,2,3,4])
print(s)

print()
print("Putting index")
s = pa.Series([1,2,3,4], index = ['*'*(i+1) for i in range(4)])
print(s)

print()
print("Accessing by index")
print(s['***'])

print("Statistics")
print(s.max())
print(s.min())
print(s.mean())

#Data Frame
print()
print("Data Frame")
data = {'eid': [101,102,103,104], 'Name':['A','B','C','D'], 'sal':[1000,2000,3000,4000]}
df = pa.DataFrame(data)
print(df)

print(df.Name)
print()
print(df['Name'])
print()

#Statistical operations
print()
print("Statistics")
print(df.mean())
print(df.max())

print()
print("Adding a new column:")
df['gender'] = ['m','m','f','f']
print(df)

print()
#Operations based on columns
print(df[df.sal>2000])

print()
print()
print("Describing the array")
#Getting all the values
#Mean, std, count, min, max, 25% 50% 75% quartiles
print(df.describe())



#Head and tail of data
print(df.head())
print()
print(df.head(1))
print()
print(df.tail())

#Dropping a columns
print("data after dropping columns")
print()
df = df.drop(['gender'], axis=1)
print(df)



#Data Loading
"""'

Text file data:
    read_csv
    read_table

Structured data (JSON, XMLm, HTML):
    It works fine with existing libraries

Excel (Depends upon xlrd and openpyxl packages)

Database:
    pandas.io.sql module(read_frame)

"""


"""

Reading and Writing data
df = pd.read_csv('abc.csv') #From csv
df = pd.read_csv('abc.txt', sep='\t') #from text file
df = pd.read)excel('mtcars.xlsx', 'Sheet2') #from excel

Readinf from multiple sheets of ame Excel into different data frames

xlsx = pd.ExcelFile('abc.xlsx')
sheet1_df = pd.read_excel(xlsx, 'Sheet1')
sheet2_df = pd.read_excel(xlsx, 'Sheet2')

"""



"""

Wrriting 
pd.to_csv('abc.csv', index=False)
pd.to_csv('abc.csv', sep = '\t', index=False)
pd.to_excel('abc.xlsx', sheet_name="'Sheet1' , index=False)

"""


"""

#Renaming a column
df.rename(columns = {'old_colname':'new_colname'}, inplace = True)

#Flag duplicates
df.duplicated()

#Drop duplicates
df = df.drop_duplicates()

"""




"""

Drop missing rows and columns having missing values
df.dropna()

Replace all missing values with 0
df.fillna(value = 0)

Check missing value condition and return boolean value true or false for each cell
pd.isnull(df)

"""

"""

Merge/ Join
 

"""



