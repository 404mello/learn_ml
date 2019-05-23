#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:59:50 2019

@author: prawigya
"""
import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a*3)
print(a==0)
print(a%2==0)
print(a.transpose())

#Matrix mul
print(a.dot(a))

#Slicing
# [ starting index of row: ending index of row , starting index of colunn : ending index of column] 
print(a[2,:])
print(a[:2, 1:3])

#Using linspace to divide the array into 7 equal parts
print(np.linspace(1,10,7))

#Zeros and ones
print(np.zeros((1,3)))
print(np.ones((4,4)))

#Identity matrixa
print(np.eye(3))

print(np.full((3,3),2))

#Advanced slicing
print(" Advanced Slicing of data ")
print(a[[0,1],[0,0]])
#a[0 row 0 column and 1 row 0 column] 

print()
print("Shape of data")
print(a.shape)

#Example of features, getting the shape of the data to match with the shape of the training 
print("Example")
from sklearn.datasets import load_digits

data = load_digits()

features = data.data

print(features.shape)

print()

#Value in an numpy array is always converted to data of higher data type
#indices() will cteate a set of arrays stacked as a one higher dim array
print()
d = np.indices((3,4))
print(d)

#Shape of the data
print("Shape of the indices array ", d.shape)
"""
G.K. 

a=012 # Will give octal representation in Python/ JAVA/ C
a = 0o12 #Will give octal rep in Python3
a=0b0101 #Will give 5 in Python3


"""

#All operators work for numpy arrays, but in matrix mul we use dot.

#Broadcasting in Python
#Storing from one type to another type
print()
print("Broadcasting")
b = np.empty_like(a) #Will copy the shape of a and put random values
v = np.array([1,0,1])
print("Adding")
for i in range(3):
    b[i :] = a[i: ]+v
print(b)

###########################

print()
print("Reshaping")
v = np.array([1,2,3])
w = np.array([4,5])
print(np.reshape(v, (3,1)) * w)
#To compute an outer product, we first reshape v to be a column vector of shape (3,1)
#We can then broadcast it against w to yeild an output of shape (3,2) which is the outer product of v and w      

###########################






