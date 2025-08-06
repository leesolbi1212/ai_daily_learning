import cv2
import sys

# VideoCapture : 동영상을 읽어오는 역할, 웹캠을 읽어오는 역할 
cap = cv2.VideoCapture('./movies/35427-407130886_tiny.mp4') # 읽을 수 있는 객체 만들기 

# 객체를 읽을 수 없는 지 확인하는 코드 
if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit() # 시스템 모듈 : 프로그램을 종료해줌

print('동영상 불러오기 성공')

# 가로, 세로, 프레임 수 출력해보기 
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS) # 1초당 보이는 프레임 수 
print(width, height, frame_count, fps)


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

'''
cv2.waitKey(delay)의 delay 인자는 프레임을 화면에 표시한 뒤 다음 프레임으로 넘어가기 전에 “얼마나 오래 대기할지(밀리초 단위)”를 결정합니다. 즉, 이 값이 크면 클수록 각 프레임 사이에 더 긴 간격을 두고 화면을 갱신하기 때문에 동영상 재생 속도가 느려집니다.

'''