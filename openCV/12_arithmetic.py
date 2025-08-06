import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/dog.jpg')
img2 = cv2.imread('./images/square.bmp')

dst1 = cv2.add(img1, img2)
# 가중치 합성 : 두 이미지를 비율로 섞어줌, 추가로 더할 상수가 있다면 더해줌 여기선 0
dst2 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0) 
dst3 = cv2.subtract(img1, img2)
# 절대 차이 : 두 이미지 간의 절대 차이값 : abs(img1(x,y)-img2(x,y))
# 예 ) img1 = 80, img2 = 100 = abs(-20) = 20 (반전값)
dst4 = cv2.absdiff(img1, img2)

img = {'dst1':dst1, 'dst2':dst2, 'dts3':dst3, 'dts4':dst4}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1]) #행, 열 다 가져오고 마지막에 색상 채널
    plt.title(k)
plt.show()