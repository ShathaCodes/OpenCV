import os
import cv2 as cv
import numpy as np

people=[]
DIR = r'C:\Users\LENOVO\Desktop\my python\OpenCV\Face_Recognition\Faces\Train'
for i in os.listdir(DIR):
    people.append(i)
haar_cascade = cv.CascadeClassifier('C:/Users/LENOVO/Desktop/my python/OpenCV/Face_Detection/haar_face.xml') # read data and store it

#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Face_Recognition/face_trained.yml')

img = cv.imread(r'C:\Users\LENOVO\Desktop\my python\OpenCV\Face_Recognition\Faces\Test\ariana2.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Person",gray)

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9) 
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img,str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("Detected Face",img)

cv.waitKey(0)