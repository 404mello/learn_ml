#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:03:29 2019

@author: prawigya
"""

import numpy as np
#import sys

a= np.array([1,2,3])

#Less memory
#Fast
#Convenient than lists


#Comparing the size of numpy array and list
#list1 = range(1000)
#print(sys.getsizeof(5)*len(list1))

array = np.arange(1000)
#print(array.size*array.itemsize)


#Basic array operations


a = np.array([[6,6,7],[1,2,3],[4,5,6]], dtype=np.float64)
#We can also use dtype = complex
print("The array is")
print(a)

print("Dimension is",a.ndim)

print("Itemisze=",a.itemsize)

print("Datatype of the array is",a.dtype)

print("Size=",a.size)
print("Shape=",a.shape)

#Initializing 
print("Zeros array")
b = np.zeros((3,4), dtype=np.int64)
print(b)
print("Ones array")
b = np.ones((3,4))
print(b)

print("Range of numbers")

r = np.arange(1,5)
r = np.arange(1,5,2)
print(r)

print("Linspace")
print(np.linspace(1,5,10))
#Generate 10 numbers bw 1 and 5 which are linearly spaced

print("Reshape")
a = np.array([[1,2],[3,4],[5,6]])
print("Initial shape = ",a.shape)
print(a)

print("\nFinal Shape")
a=a.reshape(2,3)
print(a)

print("\nRavel function will flatten the array")
c = a.ravel()
print(c)

print("Min, Max and Sum")
print("Min=",a.min(), " Max =",a.max()," Sum=",a.sum())

#Axis 0 = columns
#Axis 1= rows

print("\nPrinting axis sum of 0",a.sum(axis=0))

print("\nSquare root")
print(np.sqrt(a))

print("\nStandard Deviation of all the elements")
print(np.std(a))

