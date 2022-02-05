import cv2 as cv
import numpy as np


blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# bitwise AND
b_and = cv.bitwise_and(rectangle,circle)
cv.imshow("C and R",b_and)

# bitwise OR
b_or = cv.bitwise_or(rectangle,circle)
cv.imshow("C or R",b_or)

# bitwise XOR
b_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("C xor R",b_xor)

# bitwise NOT
b_not = cv.bitwise_not(rectangle)
cv.imshow("R not",b_not)


cv.waitKey(0)