import cv2

img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE) 
# 흑백으로 읽어와서 ndarray로 저장된다. 
print(img1)

# 트루컬러 영상
img2 = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR) 
# cv2.IMREAD_COLOR 생략 하며 기본 값이 RGB 컬러. (3개가 BGR 순서로 찍힌다.)
print(img2)

# 이미지 찍어보기 : 윈도우에 새 창이 뜨면서 이미지를 보여준다. (BGR형태로)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey() # 실행 하고 특정 키를 누를 때까지 창이 닫히지 않게 기다려줌 