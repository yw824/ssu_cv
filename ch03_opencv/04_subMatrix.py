import numpy as np
import cv2 as cv

def func4():
    img1 = cv.imread('./data/lenna.bmp', cv.IMREAD_GRAYSCALE)

    img2 = img1[200:400, 200:400]
    img3 = img1[200:400, 200:400].copy() # 부분행렬이라도 복사해야 함 
    
    img2 += 60

    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.imshow('img3', img3)

    cv.waitKey()
    cv.destroyAllWindows()

# END OF FUNC4

if __name__ == "__main__":
    func4()