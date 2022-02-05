import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #Images, Videos, Live Videos
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Live Videos
    capture.set(3,width)
    capture.set(4,height)

img = cv.imread('images/cat.jpg')   
resized_img = rescaleFrame(img,.2)
cv.imshow('Cat',resized_img)
cv.waitKey(0)