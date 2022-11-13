#pylint:disable=no-member

import cv2 as cv




if __name__ == '__main__':
    img = cv.imread('../Resources/Photos/group 1.jpg')
    cv.imshow('Group of 5 pdeople', img)
    cv.waitKey(2000)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray People', gray)
    cv.waitKey(2000)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)               # faces_rect is a list of coordnates

    print(f'Number of faces found = {len(faces_rect)}')

    for (x, y, w, h) in faces_rect:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('Detected Faces', img)

    cv.waitKey(0)