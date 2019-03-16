#Humans = biology = pattern
#Senses

#Computers = mathematical = numbers

#Images are numbers for a computer
import cv2

print("Showing an image")
#Check for gray and BGR as well
img = cv2.imread('doom.jpg', 0)
print(type(img))
print("Data type of constituents of image array is",img.dtype, "Which is unsigned integer 8 bit")
#000000 - 111111 ; 0-FF ; 0-255
print("ndarray = Composite date type, array of n-dimensions")
print("\n")
print("Shape of the image: Resolution")
print(img.shape)
print("\n")
#cv2.imshow("Charizard", img)
#cv2.waitKey(0)
# cv2.destroyAllWindows()

print("Number of dimensions of the image")
print(img.ndim)
print("\n")
print("Size of the image")
print(img.size)

print(img)
