import cv2
import numpy as np

oldx = oldy = 0

# 마우스 이벤트 함수 
def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    # print(event) 
    if event == cv2.EVENT_LBUTTONDOWN:
        print('왼쪽 버튼 누름: %d, %d' % (x, y))
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('왼쪽 버튼 뗌 : %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 이동 중 : %d, %d' % (x, y))
        if flags: # 여러 플래그를 동시에 담을 수 있음 
            print('마우스 드래그 함')
            # 선 그어주기
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3 )
            cv2.imshow('img',img)
            
            oldx, oldy = x, y

# 흰 색 이미지 띄우기 
img = np.ones((500,500,3),dtype=np.uint8) * 255
cv2.namedWindow('img') # 창이 뜰 때 이름을 부여해줌

cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 3) 
cv2.rectangle(img, (300, 200, 150, 100), (0, 255, 0), -1) # 도형 안쪽 채워짐
cv2.circle(img,(250,400),50,(255,0,0),3)
cv2.putText(img, 'Hello',(50, 300), cv2.FONT_HERSHEY_DUPLEX, 0.7, (0,0,0)) # 대상이미지, 문자열, 시작좌표, 글꼴 종류, 폰트 크기, 텍스트 색상 

cv2.imshow('img',img)
# setMouseCallback : 마우스가 어떤 행동을 하게되면 자동으로 호출되는 메서드
cv2.setMouseCallback('img', on_mouse) 
# img라는 이름을 가진 애한테 on_mouse를 실행해줌
cv2.waitKey()


