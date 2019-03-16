#Saving the image
import cv2

img =  cv2.imread('doom.jpg',0)
cv2.imwrite('Doomblack.jpg',img)
