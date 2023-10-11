import cv2 as cv

img = cv.imread('data/lenna.bmp')

if img is None:
    print("Image Load Failed")
    exit()

cv.imshow('image', img)
cv.waitKey()