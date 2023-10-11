import numpy as np
import cv2 as cv

def func1():
    img1 = cv.imread('data/cat.bmp', cv.IMREAD_GRAYSCALE) # 회색조로 읽기

    if img1 is None: 
        print('Image Load Failed')
        return
    
    print(f'type(img1) : {type(img1)}')
    print(f'img1.shape: {img1.shape}')

    if len(img1.shape) == 2:
        print('img1 is Grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is trueColor image')
    
    cv.imshow('image', img1)
    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == '__main__':
    func1()