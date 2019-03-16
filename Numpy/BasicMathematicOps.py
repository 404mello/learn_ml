#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 06:41:23 2019

@author: prawigya
"""
import numpy as np

a = np.array([[1,1],[0,1]])
b = np.array([[1,2],[3,4]])
print("A")
print(a)
print("B")
print(b)

print("\nSum")
print(a+b)

print("\nDot Product <<Is actually matrix multiplication>>")
print(a.dot(b))

print("\nIndexing and Slicing")
print("The array")
a = np.array([6,7,8])
print(a)
print("\nSlicing")
print(a[:2])
print(a[-1])

print("Multidimensional Array now")
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("\nSlicing now")
print(a[0,:2])
print("\n")
print(a[0:2,2])
print("\n",a[-1])
print("\n")
print(a[:,1:])

print("Iterating through the array")
print(a,"\n")

print("Row Traversal")
for row in a:
    print(row)
    
print("Flattening and traversing")
for cell in a.flat:
    print(cell, end=" ")
print()

print("Stacking 2 arrays together")
a = np.arange(6).reshape(3,2)
b = np.arange(6,12).reshape(3,2)
print("A")
print(a)
print("B")
print(b)

#Tuple arguements in vstack
print("Vertical Stacking")
v = np.vstack((a,b))
print(v)

h = np.hstack((a,b))
print(h,"\n")

print("Horizontal Split")

a = np.arange(30).reshape(2,15)
print("A")
print(a)

print("Splitting")
result=np.hsplit(a,3)
print(result[0])
print(result[1])
print(result[2])

print("Vertical Split")

result = np.vsplit(a, 2)
print(result[0])
print(result[1])
print("\n")
print("Indexing with Boolean Arrays")

a = np.arange(12).reshape(3,4)
print("A")
print(a)
b = a>4
print(b)
print("Boolean Indexing")
print(a[b])
print("Operating")
a[b]=-1
print(a)




