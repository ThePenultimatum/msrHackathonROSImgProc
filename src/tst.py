#!/usr/bin/python -tt

import cv2

a = cv2.VideoCapture(-1)

while(True):
    # Capture frame-by-frame
    ret, frame = a.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

a.release()
cv2.destroyAllWindows()
