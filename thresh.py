import cv2 as cv

#thresholding = binarization of an img : pixels = 0/1

img = cv.imread('images/cat.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Cat",img)
gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Simple Thresholding
threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY) # , the less thresh val, the more white u get,set max_pix to 255, else 0
cv.imshow("Simple Threshold",thresh)

threshold , thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("Inverted Threshold",thresh_inv)

# Adapted Thresholding : computer finds the optimal thresholding value
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)# type : mean/gaussian, blocksize = kernel size, C is substracted from mean to finetune to improve accuracy
cv.imshow("Adaptive",adaptive_thresh)


cv.waitKey(0)