#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:49:38 2019

@author: prawigya
"""

import cv2
import sys
cascadepath = 'haarcascade_frontalface_alt.xml'
facedetector = cv2.CascadeClassifier(cascadepath)
#cam = cv2.VideoCapture("dinner.mp4")
cam = cv2.VideoCapture(0)
while True:
    rect, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = facedetector.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow('faces', img)
    if(cv2.waitKey(1) == ord('a')):
        break
cam.release()

        
    
    
    