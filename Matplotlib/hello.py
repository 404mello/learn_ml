#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 13:02:52 2019

@author: prawigya
"""

#Matplotlib graphs: Univariant (plot, bar, box, hist) and multivariant:  (scatter, corr-coeff)
#Matplotlib is used for creating plots and charts
import matplotlib.pyplot as plt
import numpy as np
myarray = np.array([1,2,3])
plt.plot(myarray)
plt.xlabel('Some x axis')
plt.ylabel('Some y axis')
plt.show()
#############

x = np.array([1,2,3])
y = np.array([2,4,6])

plt.scatter(x, y)
plt.xlabel('Some x axis')
plt.ylabel('Some y axis')
plt.plot(x, y)
plt.show()
#############


