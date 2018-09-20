#!/usr/bin/python -tt

import cv2

a = cv2.VideoCapture(-1)

colorsToTrack = []

def avgColors(block):
    return 1

def getColors(circle, imgArr):
    print circle
    [[x, y, rad]] = circle
    maxX = len(imgArr)
    maxY = len(imgArr[0])
    blockHalfSize = 2
    minXToUse = int(x)-blockHalfSize
    minYToUse = int(y)-blockHalfSize
    maxXToUse = int(x)+blockHalfSize
    maxYToUse = int(y)+blockHalfSize
    if minXToUse < 0:
        minXToUse = 0
    if minYToUse < 0:
        minYToUse = 0
    if maxXToUse >= maxX:
        maxXToUse = maxX-1
    if maxYToUse >= maxY:
        maxYToUse = maxY-1
    block = imgArr[minXToUse:maxXToUse, minYToUse:maxYToUse]
    #print [minXToUse, maxXToUse], [minYToUse, maxYToUse]
    print imgArr[minXToUse:maxXToUse,minYToUse:maxXToUse]
    print block
    return avgColors(block)

while(True):
    # Capture frame-by-frame
    ret, frame = a.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    newImg = gray
    if colorsToTrack == []:
        cs = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 200)#, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]])
        if cs is not None:
            for c in cs:
                [[x, y, rad]] = c
                newImg = cv2.circle(gray, (y, x), rad, (255, 0, 0), 3)

    print cs
    # Display the resulting frame
    cv2.imshow('frame',newImg) #frame)#gray)
    #print frame[0:20][0:20]
    #if cs is not None:
    #    colors = []
    #    for c in cs:
    #        colors.append(getColors(c, frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

a.release()
cv2.destroyAllWindows()
