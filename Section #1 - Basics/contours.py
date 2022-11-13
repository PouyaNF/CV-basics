#pylint:disable=no-member
import cv2 as cv
import numpy as np



if __name__ == '__main__':
    img = cv.imread('../Resources/Photos/cats.jpg')
    cv.imshow('Cats', img)
    cv.waitKey(2000)

    blank = np.zeros(img.shape, dtype='uint8')
    cv.imshow('Blank', blank)
    cv.waitKey(2000)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)
    cv.waitKey(2000)

    blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)
    cv.waitKey(2000)

    canny = cv.Canny(blur, 125, 175)
    cv.imshow('Canny Edges', canny)
    cv.waitKey(2000)
    # ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    # cv.imshow('Thresh', thresh)

    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # contours are useful for object detection
    print(f'{len(contours)} contour(s) found!')

    cv.drawContours(blank, contours, -1, (0, 0, 255), 1)    #-1 : shows all contours   , color is BGR : (0,0,255) , 1 : ticknesss level
    cv.imshow('Contours Drawn', blank)

    cv.waitKey(2000)