#pylint:disable=no-member

import cv2 as cv
import numpy as np


if __name__ == '__main__':
    img = cv.imread('../Resources/Photos/park.jpg')
    cv.imshow('Park', img)

    blank = np.zeros(img.shape[:2], dtype='uint8')

    b, g, r = cv.split(img)

    cv.imshow('Blue-split', b)      # show it as grayscaled images showing the intensity of blue channel pixels
    cv.imshow('Green-split', g)
    cv.imshow('Red-split', r)


    blue = cv.merge([b, blank, blank])
    green = cv.merge([blank, g, blank])
    red = cv.merge([blank, blank, r])

    cv.imshow('Blue', blue)                  # lighter portion of the merged image represents high level of blue pixels on that portion
    cv.imshow('Green', green)
    cv.imshow('Red', red)

    print(img.shape)
    print(b.shape)
    print(g.shape)
    print(r.shape)

    merged = cv.merge([b, g, r])
    cv.imshow('Merged Image', merged)

    cv.waitKey(0)