#pylint:disable=no-member
import cv2 as cv
import os

#cwd = os.getcwd()
#print(cwd)

if __name__ == '__main__':
    # Read in an image
    path = '../Resources/Photos/park.jpg'
    img = cv.imread(path)
    cv.imshow('Park', img)
    cv.waitKey(2000)

    # Converting to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)
    cv.waitKey(2000)


    # Blur  - help to reduce some of the noise in an image
    blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)  # (7,7) is the window size
    cv.imshow('Blur', blur)
    cv.waitKey(2000)

    # Edge Cascade - to detect edges
    canny = cv.Canny(blur, 125, 175)  #
    cv.imshow('Canny Edges', canny)
    cv.waitKey(2000)

    # Dilating the image
    dilated = cv.dilate(canny, (7, 7), iterations=3)
    cv.imshow('Dilated', dilated)
    cv.waitKey(2000)

    # Eroding
    eroded = cv.erode(dilated, (7, 7), iterations=3)
    cv.imshow('Eroded', eroded)
    cv.waitKey(2000)

    # Resize
    resized = cv.resize(img, (500, 500),
                        interpolation=cv.INTER_CUBIC)  # (500,500) is the target size ,  INTER_AREA : for dimensions that are smaller from the original dimensions
    cv.imshow('Resized',
              resized)  # is for INTER_LINEAR , INTER_CUBIC is for enlarging the image  - second one is slower but more accurate
    cv.waitKey(2000)

    # Cropping
    cropped = img[50:200, 200:400]
    cv.imshow('Cropped', cropped)
    cv.waitKey(2000)