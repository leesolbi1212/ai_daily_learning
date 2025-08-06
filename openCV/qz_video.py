import cv2
import sys

cap1 = cv2.VideoCapture('./movies/woman.mp4') 
cap2 = cv2.VideoCapture('./movies/sea.mp4')   

# 2) 프레임 속성 가져오기 (cap1 기준)
width  = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap1.get(cv2.CAP_PROP_FPS)

# 3) 크로마키 색 설정
lower_green = (50, 150, 0)
upper_green = (85, 255, 255)

while True:
    ret1, frame1 = cap1.read()  # 크로마키 프레임
    ret2, frame2 = cap2.read()  # 배경 프레임
    if not (ret1 and ret2):
        break

    # 2) frame1에서 초록~연두만 흰색(255), 나머지는 검정(0)인 mask 생성
    hsv  = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    # → mask==255인 픽셀 위치 = “초록 배경” 영역

    # 3) mask가 255인 위치에 한해…
    #    src=frame2 픽셀을 dst=frame1에 덮어쓴다
    cv2.copyTo(frame2, mask, frame1)
    # 첫번째 파라미터를 mask의 흰색인 위치에만 세번째 파라미터에 덮어쓴다.

    # 6) 결과 보여주기
    cv2.imshow('Chroma Key Composite', frame1)
    if cv2.waitKey(10) == 27: 
        break    
frame1.release()
