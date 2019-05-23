import numpy as np
import cv2

img = cv2.imread('doom.jpg', cv2.IMREAD_COLOR)

img[55, 55] = [0,0,0]
px = img[55,55] #Location of pixel
#print(px)

#ROI: Region of image
roi = img[100:150, 100:150]
#img[100:150, 100:150] = [0,0,0]

dragon_face = img[129:316 , 228:299]
#316-129 = 187 ; 299-228 = 71
#xlast = 569 ylast = 805

#img[0:187, 0:71] = dragon_face
x=0
y=0
c=0

"""
while(True):
    if(y+71> 433):
        break
    img[x: x+187, y: y+71] = dragon_face
    c+=1
    print(c,' ',x, ' ',y)
    x=x+188
    if(x+187>569):
        x=0
        y =y+72

#A lot of heads
"""

cv2.imshow('Oasd',img)
cv2.imshow('asd',dragon_face)
cv2.waitKey(0)
cv2.destroyAllWindows()
