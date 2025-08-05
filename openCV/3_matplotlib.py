import cv2
import matplotlib.pyplot as plt

# subplot이용하여 left plot에는 그레이스케일 영상, right plot에는 컬러영상을 출력
img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE) # ndarray로 저장 (흑백)
img_color = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR) #ndarray로 저장 (컬러) 그러나 색상이 이상하게 찍힘 (스머프처럼 찍혀버림, BGR이기 때문)

img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB) # BGR을 RGB로 바꿔줌

plt.subplot(121) # 1행 2열짜리 1번째 (=plt.subplot(1,2,1))
plt.axis('off') # 격자 없애기
plt.imshow(img_gray, cmap='gray') # 흑백 출력 

plt.subplot(122) # 1행 2열짜리 2번째 (=plt.subplot(1,2,2))
plt.axis('off')
plt.imshow(img_color) # 컬러 출력
plt.show()