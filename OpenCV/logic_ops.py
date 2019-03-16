import cv2
import numpy as np

#Same size image
img1 = cv2.imread('blastoise.png')
img2 = cv2.imread('venasaur.jpg')

img3 = cv2.imread('mew.png')
#Addition operation
#add = img1 + img2

#The pixels get scalarly added
#add = cv2.add(img1, img2)

#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) #0.6-0.4 -> %age of weight added. 0 is the gamma value

#We can also use ROI
rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

#We make a mask of the logo and generate it
img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
#Using a threshold
ret, mask = cv2.threshold(img2gray, 125, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask = mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst



cv2.imshow('img3',img3)
cv2.imshow('img1',img1)
cv2.imshow('mask',mask)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img3_fg',img3_fg)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
