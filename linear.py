#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:53:48 2019

@author: prawigya
"""
import math
feature = [100,200,300,400]
labels = [500,1100,1700,2300]
mean = sum(feature)
mean = mean/len(feature)

meanx = mean

meany = sum(labels)/len(labels)

y=labels

x=feature
#x1 = x-xmean
x1 = [i - meanx for i in x]

#y1 = y-ymean
y1 = [i-meany for i in y]

#x2 = (x - xmean)**2
#y2 = (y - ymean)**2
x2 = [i**2 for i in x1]
y2 = [i**2 for i in y1]
z = [x1[i]* y1[i] for i in range(len(x))]

r = sum(z)/(math.sqrt(sum(x2))*math.sqrt(sum(y2)))
print(r)

#Standard deviations x and y
sx = math.sqrt(sum(x2)/(len(x2)-1))
sy = math.sqrt(sum(y2)/(len(y2)-1))

b = (sy/sx)*r
print("b is",b)

a = meany - b*meanx
print("a is",a)

# y = a + b*x
print("Taking sample as 160")

y = a + b*160
print("The value for 160 is",y)