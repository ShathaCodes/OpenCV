import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('images/cat.jpg')
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Cat",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale",gray)

#Grayscale histogram
gray_hist = cv.calcHist([gray],[0],None,[256],[0,256])

#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel("Bins: interval of pixel intensity")
#plt.ylabel('Nbr of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

# Color Histogram
mask = cv.circle(blank,(img.shape[1]//2+100,img.shape[0]//2),100,255,-1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("Mask",masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel("Bins: interval of pixel intensity")
plt.ylabel('Nbr of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)