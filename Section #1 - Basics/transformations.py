import cv2 as cv
import numpy as np


def read_image(image_path, wait):
    # Reading images
    img = cv.imread(image_path)
    cv.imshow('Cats', img)
    cv.waitKey(wait)                # wait for  ..  milisecond
    cv.destroyAllWindows()


def read_video(video_path, wait):
    # Reading Videos
    capture = cv.VideoCapture(video_path)
    while True:
        isTrue, frame = capture.read()
        if isTrue:
            cv.imshow('Video', frame)
            if cv.waitKey(wait) & 0xFF == ord('d'):  # wait for wait milliseconds for new frame . 'd' key for break
                break
        else:  # if video reaches to the end frame, break
            break
    capture.release()
    cv.destroyAllWindows()


def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def resize_video(video_path, scale=0.5):
    capture = cv.VideoCapture(video_path)
    while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame, scale)

        # cv.imshow('video', frame)
        # cv.imshow('resized video', frame_resized)
        if isTrue:
            cv.imshow('Video', frame)
            cv.imshow('Rescaled Video', frame_resized)
            if cv.waitKey(20) & 0xFF == ord('d'):
                break
        else:  # if video reaches to the end frame, break
            break
    capture.release()
    cv.destroyAllWindows()




def rotate(img, angle, rotPoint=None):  # rotPoint is the point of rotation
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)  # default rotate around the center of the picture
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)  # 1.0 is the scal value
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


def translate(img, x, y):
    # shift the image using translation matrix
    # -x --> Left
    # -y --> Up
    # x --> Right
    # y --> Down
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


if __name__ == '__main__':
    image_path = '../Resources/Photos/cat.jpg'
    video_path = '../Resources/Videos/kitten.mp4'



    # read_video(video_path, 20)
    # resize_video(video_path)
