import cv2
import sys

# 웹캠을 연결할 것 (0) : 첫 번째 카메라 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라 열 수 없음')
    sys.exit()
    
print('카메라 연결 성공')

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(w,h,fps)

while True:
    ret, frame = cap.read() # 프레임 1장을 가져오는 것 
    # ret에는 True/False가 들어가게 되고, frame에는 이미지 자체가 ndarray로 들어가게 된다. 
    if not ret:
        break
    cv2.imshow('frame',frame)
    if cv2.waitKey(10)==27: 
        # waitKey(10) 안에 숫자를 안넣어주면.. 영상 재생이 안된다. 
        break
cap.release()