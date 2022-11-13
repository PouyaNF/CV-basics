
import cv2 as cv
import numpy as np


if __name__ == '__main__':
    blank = np.zeros((400, 400), dtype='uint8')

    rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
    circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
    cv.waitKey(2000)

    cv.imshow('Rectangle', rectangle)
    cv.imshow('Circle', circle)
    cv.waitKey(2000)

    # bitwise AND --> intersecting regions
    bitwise_and = cv.bitwise_and(rectangle, circle)
    cv.imshow('Bitwise AND', bitwise_and)
    cv.waitKey(2000)

    # bitwise OR --> non-intersecting and intersecting regions
    bitwise_or = cv.bitwise_or(rectangle, circle)
    cv.imshow('Bitwise OR', bitwise_or)
    cv.waitKey(2000)

    # bitwise XOR --> non-intersecting regions
    bitwise_xor = cv.bitwise_xor(rectangle, circle)
    cv.imshow('Bitwise XOR', bitwise_xor)
    cv.waitKey(2000)

    # bitwise NOT
    bitwise_not = cv.bitwise_not(circle)
    cv.imshow('Circle NOT', bitwise_not)

    cv.waitKey(0)