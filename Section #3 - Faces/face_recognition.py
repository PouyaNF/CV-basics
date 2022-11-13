#pylint:disable=no-member

import numpy as np
import cv2 as cv


if __name__ == '__main__':


    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
    # features = np.load('features.npy', allow_pickle=True)
    # labels = np.load('labels.npy')


############### classifier loading
    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.read('face_trained.yml')

############# Read image & turn it to gray
    img = cv.imread(r'../Resources\Faces\val\madonna/4.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #cv.imshow('Person', gray)

######### # Detect the face in the image
    faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4) # 4 is minimum neighbours
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y + h, x:x + w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}')

        cv.putText(img, str(people[label]), (30, 40), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=2)
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Face', img)

    cv.waitKey(0)