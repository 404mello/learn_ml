import cv2
import numpy as np
#Erosion and Dilation
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read() #_ is dont care value returned from a function
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)   #hue saturation value

    #We have to select our own values for the colour we want to filter0
    lower_green = np.array([35,100,0])
    upper_green = np.array([50,255,255])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((5,5), np.uint8)
    #Erosion and Dilation
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    #Opening and Closing
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)


    #cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    #cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()
