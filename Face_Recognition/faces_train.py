import os
import cv2 as cv
import numpy as np

people=[]
DIR = r'C:\Users\LENOVO\Desktop\my python\OpenCV\Face_Recognition\Faces\Train'
for i in os.listdir(DIR):
    people.append(i)
haar_cascade = cv.CascadeClassifier('C:/Users/LENOVO/Desktop/my python/OpenCV/Face_Detection/haar_face.xml') # read data and store it

features = []
labels =[]

def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=9)
            for (x,y,w,h) in faces_rect:
                faces_roi= gray[y:y+h,x:x+w]
                # mapping by index in the list
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training Done")
features = np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
#Train the recognizer on the features list and the labels list
face_recognizer.train(features,labels)
face_recognizer.save('Face_Recognition/face_trained.yml')

np.save("Face_Recognition/features.npy",features)
np.save("Face_Recognition/labels.npy",labels)