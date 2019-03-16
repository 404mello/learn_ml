import numpy as np
import cv2

img = cv2.imread('doom.jpg', cv2.IMREAD_COLOR)
#Drawing a line
cv2.line(img, (0,0), (150,150), (0,0,0), 15) #(255,255,255) color; coordinates are (0,0) and (150,150) 15 is the lindwidth

#Drawing a rectangle
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5) #Top left coordinates, bottom right coordinates, width, color

#Drawinig a circle
cv2.circle(img, (100,63), 55, (0,0,255), -1 ) #Center of circle coords, radius, width.. a -ve will fill the circle

#Drawing a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3) #T is for connecting the final point to the first point

#Write
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Charizard', (0,130), font, 1, (0,0,0), 2, cv2.LINE_AA ) #(0,130) is the starting coord #1 is the size #2 is the thickness

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
