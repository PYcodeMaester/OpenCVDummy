import cv2
import numpy as np

capture = cv2.VideoCapture(0)

res,frame1 = capture.read()
res,frame2 = capture.read()

while capture.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, threshold = cv2.threshold(blur, 20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(threshold,None,iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 10000:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(120,200,200),4)
    # cv2.drawContours(frame1, contours,-1,(0,255,255),2)

    cv2.imshow("video", frame1)
    frame1 = frame2
    ret,frame2 = capture.read()
    if(cv2.waitKey(40) == 27):
        break

cv2.destroyAllWindows()
capture.release()