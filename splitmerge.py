import cv2 as cv
import numpy as np

img = cv.imread('images/park.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')

#split the image into 3 color channels
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow("Red",r)
cv.imshow("Green",g)

print(img.shape) # (367, 550, 3) where 3 color channel
print(b.shape) # (367, 550) it has 1 which is for greyscale

#merge the color channels to reconstruct the image
merged = cv.merge([b,g,r])
cv.imshow("Merged",merged)

cv.waitKey(0)