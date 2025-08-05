import cv2
import numpy as np

# 흑백 이미지 
img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
print('img_gray type: ', type(img_gray)) # <class 'numpy.ndarray'>
print('img_gray shape: ', img_gray.shape) # (364, 548)
print('img_gray dtype: ', img_gray.dtype) # uint8 (8비트짜리 int) = 밝기 정보

# 컬러 이미지 
img_color = cv2.imread('./images/dog.bmp')
print('img_color type: ', type(img_color)) # <class 'numpy.ndarray'>
print('img_color shape: ', img_color.shape) # (364, 548, 3) = 세로, 가로, 채널 
print('img_color dtype: ', img_color.dtype) # uint8 (8비트짜리 int) = 밝기 정보

h, w = img_color.shape[:2] # 색상 말고, 크기만 출력
print(f'이미지 사이즈: {w}*{h}') # 548*364

# 그레이스케일 영상인지, 컬러영상인지 구분하기 : shape의 채널이 3인지 2인지 
if len(img_color.shape) == 3:
    print('컬러 영상')
elif len(img_color.shape) == 2:
    print('그레이스케일 영상')
    
img1 = np.zeros((240,320,3), dtype=np.uint8) # 검정이미지로 만들었다가
img1[:,:] = (255, 102, 255) # 색을 입혀줄 수도 있음

img2 = np.empty((240,320), dtype=np.uint8) # 랜덤한 값으로 크기만 맞춰서 만들어달라 

img3 = np.ones((240,320), dtype=np.uint8) * 120 # 120을 곱하면 검정색에서 약간 밝아진다. 

img4 = np.full((240,320,3),(255, 102, 255), dtype=np.uint8)

# img_color에 특정 색 정보로 영상을 출력
# BGR: (255, 102, 255)
'''
for x in range(h):
    for y in range(w):
        img_color[x, y] = (255, 102, 255)
'''
# img_color[:,:] = (255, 102, 255) 
# 모든 픽셀에 B=255, G=102, R=255 값을 할당 (바꿔준 것, 덮은 게 아님)



cv2.imshow('img_color', img_color)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3) 
cv2.imshow('img4',img4) 

# 무한루프 돌리기 
while True:
    keyvalue = cv2.waitKey() # 어떤 값을 받으면 keyvalue에 저장
    # 어떤 키냐고 물어보기
    # ord : 아스키코드로 변환해주는 메서드
    if keyvalue == ord('i') or keyvalue == ord('I'):
        img_color = ~img_color # 값을 반전 (색상이 반전됨)
        cv2.imshow('img_color', img_color) # 새로 띄워지는 게 아니라 창이 바뀜
    elif keyvalue == 27: # 27 : esc키 
        break

