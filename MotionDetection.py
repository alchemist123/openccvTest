import cv2
import numpy as np

cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()
while True:
    diff=cv2.absdiff(frame1,frame2) #diff to contour is used to find the difference between 2 frames.
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contour,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contours in contour:
        (x,y,w,h)=cv2.boundingRect(contours)
        if cv2.contourArea(contours)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"status:{}".format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    # cv2.drawContours(frame1,contour,-1,(0,255,0),2)

    cv2.imshow('motion',frame1)
    frame1=frame2
    ret,frame2=cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()