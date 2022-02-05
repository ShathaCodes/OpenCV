import cv2 as cv
import numpy as np

img = cv.imread('images/cat.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# First Method
blur = cv.GaussianBlur(gray,(7,7), cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)
cv.imshow("Canny edges",canny)

# Second Method
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) # hierarchies: find contours withion contours,RETR_LIST : retrievs all the contours != RETR_EXTERNAL != RETR_TREE by hierarchy, CHAIN_APPROX_NONE : all the coordinate of the contours

print(len(contours))

cv.drawContours(blank,contours,-1,(125,70,102),1)
cv.imshow('Contours Drawn',blank)



cv.waitKey(0) #close when tap key
