#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:07:08 2019

@author: prawigya
"""
import cv2
import numpy as np
#import matplotlib.pyplot as plt

img = cv2.imread('doom.jpg', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('doom.jpg', 0)
#IMREAD_GRAYSCALE = 0
#IMREAD_COLOR =1
#IMREAD_UNCHANGED = -1

cv2.imshow('Death', img)
cv2.waitKey()
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation = 'bicubic')
#plt.plot([50, 100],[200, 100], 'c', linewidth=5)
#plt.show()

#cv2.imwrite('gray_char.jpg', img)
