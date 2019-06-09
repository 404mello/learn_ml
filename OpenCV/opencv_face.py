#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:36:34 2019

@author: prawigya
"""
import cv2
imgpath = 'Prawigya.jpg'
cascadepath = 'haarcascade_frontalface_alt.xml'
facecasspath = cv2.CascadeClassifier(cascadepath)
image = cv2.imread(imgpath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face = facecasspath.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=10, minSize = (25,25))
for(x, y, w, h) in face:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow("Face Found", image)
cv2.waitKey(0)