import cv2
import numpy
import matplotlib.pyplot as plt

img = cv2.imread('doom.jpg')

cv2.imshow('Window',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
