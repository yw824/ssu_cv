import numpy as np
import cv2


def calcGrayHist(img):
    channels = [0]
    histSize = [256]
    histRange = [0, 256]

    # 입력 영상 리스트 / 히스토그램을 구할 채널을 나타내는 리스트 - 각 이미지 당 하나씩 할당 / 
    # 마스크 영상 
    # 히스토그램 각 차원의 크기(bin의 개수)를 나타내는 리스트
    # 히스토그램 각 차원의 최솟값과 최댓값으로 구성된 리스트
    hist = cv2.calcHist([img], channels, None, histSize, histRange)

    return hist


def getGrayHistImage(hist):
    histMax = np.max(hist)

    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist


def histgoram_stretching():
    src = cv2.imread('./data/hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('histogram_stretching: Image load failed!')
        return

    # gmin = float(np.min(src))
    # gmax = float(np.max(src))
    gmin, gmax, _, _ = cv2.minMaxLoc(src)

    # histogram_stretching : (src(x, y)-Gmin)/(Gmax-Gmin) * 255
    dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src))) # 히스토그램 그래프를 담고 있는 영상 

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


def histgoram_equalization():
    src = cv2.imread('./data/hawkes.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('histogram_equalization: Image load failed!')
        return

    dst = cv2.equalizeHist(src)

    cv2.imshow('src', src)
    cv2.imshow('srcHist', getGrayHistImage(calcGrayHist(src)))

    cv2.imshow('dst', dst)
    cv2.imshow('dstHist', getGrayHistImage(calcGrayHist(dst)))

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    histgoram_equalization()
