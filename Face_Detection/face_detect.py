import cv2 as cv
from cv2 import rectangle

img = cv.imread('images/shatha.jpg')
#img = img[50:800,200:800]
img = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Lady",img)

# Face detection : looks for object in an image 
# haar cascades are really sensitive to noise in an image
# not very advanced, but easy to use and popular

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('C:/Users/LENOVO/Desktop/my python/OpenCV/Face Detection/haar_face.xml') # read data and store it
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6) #detects face and return coordinates of the face, the less minNeighbors, the more faces you'll find 

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Rectangle",img)

cv.waitKey(0)