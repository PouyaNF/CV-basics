#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt




if __name__ == '__main__':
    img = cv.imread('../Resources/Photos/park.jpg')  # read images as BGR format but outside opencv it is normally RGB
    cv.imshow('Park', img)    # cv.imshow turns BGR to RGB
    plt.imshow(img)     # img is readed as BGR and plt.imshow , show it as BGR
    plt.show()

    # BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)

    # BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow('HSV', hsv)

    # BGR to L*a*b
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow('LAB', lab)

    # BGR to RGB
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow('RGB', rgb)

    # HSV to BGR
    lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
    cv.imshow('LAB --> BGR', lab_bgr)

    cv.waitKey(0)

