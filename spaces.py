import cv2 as cv

img = cv.imread('images/park.jpg')

# BGR to Greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
# HSV to BGR
bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',bgr)


# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitKey(0)