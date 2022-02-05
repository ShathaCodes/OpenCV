import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#   1/ Paint the img a certain color
# blank[:]=0,255,0
#   Paint a square
blank[200:300,300:400]=190,18,67
#cv.imshow('Green',blank)

#   2/ Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(142,200,13),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank)

#   3/ Draw a circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(30,25,255),thickness=3)
#cv.imshow('Circle',blank)

#   4/ Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(125,75,201),thickness=2)
#cv.imshow('Line',blank)

#   5/ Write Text
cv.putText(blank,'Hello!',(300,400),cv.FONT_HERSHEY_TRIPLEX,1.0,(125,75,201),2)
cv.imshow('Text',blank)


cv.waitKey(0)