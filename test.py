import cv2
import numpy as np

img = cv2.imread('lena.jpg', -1) #imread(<file name>,1/0/-1) using for read image
print(img)
cv2.imshow('image', img) #imshow is used to show image in the img and first argument is used to visable a name in the show in title bar
key = cv2.waitKey(0) #waitkey is a method is used to hold the image in specfied time and if the argument is 0 it will waiting forthe closing key
if key == 27:
    cv2.destroyAllWindows() # it is used to destroy the window
elif key == ord('s'):
    cv2.imwrite('lenacop.png', img) #imwrite is used to save the image