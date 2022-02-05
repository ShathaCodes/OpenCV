#Read Images & Videos

import cv2 as cv

#read img
img = cv.imread('images/cat.jpg')
cv.imshow('Cat',img)
cv.waitKey(0) #close when tap key


#read video
capture = cv.VideoCapture("videos/vid.mp4")
while True:
    isTrue,frame = capture.read
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

