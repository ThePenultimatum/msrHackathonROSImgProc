#!/usr/bin/python -tt

import numpy as np
import cv2

a = cv2.VideoCapture(-1)



def contoursOnPicture(img):
    colorMinThresh = [0, 0, 150]
    colorMaxThresh = [50, 50, 255]

    print img
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    red = cv2.inRange(img, np.array(colorMinThresh), np.array(colorMaxThresh))

    newRed = cv2.medianBlur(red, 11)
    #newRed = cv2.bilateralFilter(red, 10, 5, 10)

    #d = cv2.SimpleBlobDetector_create()
    #keypoints = d.detect(red)

    #kp = cv2.drawKeypoints(red, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    im2, contours, hierarchy = cv2.findContours(newRed, cv2.RETR_EXTERNAL, 2)#cv2.CHAIN_APPROX_SIMPLE)
    print "contours:", contours
    newim = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    enclosingCircles = map(lambda cont: cv2.minEnclosingCircle(cont), contours)
    print enclosingCircles
    finimg = newim
    for c in enclosingCircles:
        (x,y) = c[0]
        finimg = cv2.circle(finimg, (int(x),int(y)), int(c[1]), [0, 255, 0], 3)
    # Display the resulting frame
    cv2.imshow('frame',finimg)
    return finimg

while(True):
    # Capture frame-by-frame
    ret, frame = a.read()
    print frame
    contoursOnPicture(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

a.release()
cv2.destroyAllWindows()
