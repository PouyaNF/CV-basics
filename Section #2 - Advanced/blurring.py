import cv2 as cv


if __name__ == '__main__':
    img = cv.imread('../Resources/Photos/cats.jpg')
    cv.imshow('Cats', img)
    cv.waitKey(2000)

    # Averaging
    average = cv.blur(img, (3, 3))
    cv.imshow('Average Blur', average)
    cv.waitKey(2000)

    # Gaussian Blur
    gauss = cv.GaussianBlur(img, (3, 3), 0)             # less blured but more natural compared to averaging
    cv.imshow('Gaussian Blur', gauss)
    cv.waitKey(2000)

    # Median Blur
    median = cv.medianBlur(img, 3)
    cv.imshow('Median Blur', median)
    cv.waitKey(2000)

    # Bilateral
    bilateral = cv.bilateralFilter(img, 10, 35, 25)
    cv.imshow('Bilateral', bilateral)
    cv.waitKey(0)