import numpy as np
import cv2 as cv

def func5():
    img1 = cv.imread('./data/cat.bmp')

    if img1 is None:
        print("Image load Failed")
        return
    
    print(img1.shape) # (480, 640, 3)
    
    img2 = 255 - img1[130:350, 200:550]
    
    cv.imshow('img1', img1)
    cv.imshow('img2', img2)
    cv.waitKey()
    cv.destroyAllWindows()

## END OF FUNC5

if __name__ == "__main__":
    func5()