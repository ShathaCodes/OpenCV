import cv2 as cv
import numpy as np

img = cv.imread('images/cat.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Cat",img)

gray  = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian : the edges are drawn over and lightly smudged
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

# Sobel : compute gradients in 2 directions
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined = cv.bitwise_or(sobelx,sobely)
cv.imshow("sobelx",sobelx)
cv.imshow("sobely",sobely)
cv.imshow("combined ",combined)

canny = cv.Canny(gray,150,150) # uses sobel to compute gradients
cv.imshow("canny ",canny)


cv.waitKey(0)