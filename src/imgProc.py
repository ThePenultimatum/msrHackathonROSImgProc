#!/usr/bin/python -tt

import numpy as np
import cv2

a = cv2.VideoCapture(-1)

while(True):
    # Capture frame-by-frame
    ret, frame = a.read()
    colorMinThresh = [0, 0, 150]
    colorMaxThresh = [75, 75, 255]

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    red = cv2.inRange(frame, np.array(colorMinThresh), np.array(colorMaxThresh))

    #d = cv2.SimpleBlobDetector_create()
    #keypoints = d.detect(red)

    #kp = cv2.drawKeypoints(red, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    im2, contours, hierarchy = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    newim = cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    # Display the resulting frame
    cv2.imshow('frame',newim)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

a.release()
cv2.destroyAllWindows()
