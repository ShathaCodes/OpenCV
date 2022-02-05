import cv2 as cv

img = cv.imread('images/cat.jpg')

# Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

# Crop
cropped = resized[50:200,200:400]
cv.imshow("Cropped",cropped)

# Greyscale
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur : remove noise
blur = cv.GaussianBlur(resized,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade
canny = cv.Canny(blur,125,175) # we put blur in here to remove some of the edges
cv.imshow('Canny',canny)

# Dilating the img
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow("Dilated",dilated)

# Eroding
eroded = cv.erode(dilated, (7,7),iterations=3)
cv.imshow("Eroded",eroded)

cv.waitKey(0) 