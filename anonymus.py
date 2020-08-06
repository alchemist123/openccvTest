import cv2
img=cv2.imread('lena.jpg',1)
img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
img=cv2.arrowedLine(img,(0,0),(255,255),(0,0,255),5)

cv2.imshow('frame',img)

cv2.waitKey(0)
cv2.destroyAllWindows()