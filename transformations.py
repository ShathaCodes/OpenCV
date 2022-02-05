import cv2 as cv
import numpy as np

img = cv.imread('images/cat.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)

# Translate
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,100,100)
cv.imshow("Translated",translated)

# Rotate
def rotate(img, angle, rotPt=None):
    (height,width) = img.shape[:2]
    if rotPt is None:
        rotPt = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPt,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow("Rotated",rotated)

# Flip
flipped = cv.flip(img,1)  #0: vert , 1 : horz , -1 :both
cv.imshow("Flipped",flipped)


cv.waitKey(0)