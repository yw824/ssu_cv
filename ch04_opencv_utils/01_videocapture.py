import cv2 as cv

cap = cv.VideoCapture(0)
# 스마트폰에는 렌즈 여러 개 있음 
# 그래서 어떤 렌즈 사용 중인 지 확인해야 함 
if not cap.isOpened():
    print("Camera open failed")
    exit()

print("Frame width:", int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print("Frame Heigth: ", int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))