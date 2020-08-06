import cv2
import datetime
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("date.avi",fourcc,20.0,(640,480))
cap.set(3,3000)
cap.set(4,3000)
while True:
    rte,frame=cap.read()
    if rte==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text='Width:'+ str(cap.get(3))+ 'Height:' + str(cap.get(4))
        #text='hello'
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,15),font,1,(255,0,0),2,cv2.LINE_AA)
        out.write(frame)
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()