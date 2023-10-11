import numpy as np
import cv2 as cv

def func3():
    img1 = cv.imread('data/cat.bmp')
    
    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255) # yellow

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)

    cv.waitKey()
    cv.destroyAllWindows()

# END OF FUNC3


if __name__ == "__main__":
    func3()