import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ is dont care value returned from a function
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #hue saturation value


    #We have to select our own values for the colour we want to filter0
    lower_green = np.array([35,100,0])
    upper_green = np.array([50,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    #Smoothing
    kernel = np.ones((15,15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)

    #Gaussian blur
    blur = cv2.GaussianBlur(res, (15,15), 0)

    #Median Blur
    median = cv2.medianBlur(res, 15)

    #Bilateral blur
    bilateral = cv2.bilateralFilter(res, 15, 75, 75)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('median', median)
    #cv2.imshow('blur', blur)
    #cv2.imshow('smoothed', smoothed)
    cv2.imshow('bilateral', bilateral)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
