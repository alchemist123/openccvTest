import cv2

cap = cv2.VideoCapture(0) # cap veriable consist of vedio from my web cam
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Define the codec and create VideoWriter object ,it is resluction
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) # creating a video writer objet which consist of save file name.avi/mp4 etc fourcc ,no: of frames per sec, hieght and width of frame
while ( cap.isOpened() ) :  #create a infinate loop to capture frame in sec, otherwise use True in the cap.isOpened()
    ret, frame = cap.read() #here is reading cap and asign in frame and ret consist of t/f which means vedio is avilable or not
    if ret == True: # if ret is true save or write the frame because the frame consist the video data.
        out.write(frame) #
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else :
        break
cap.release()
out.release()
cv2.destroyAllWindows()
