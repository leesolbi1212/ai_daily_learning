import cv2
import matplotlib.pyplot as plt



# 색 채널 분리해보기
img1 = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)

# 히스토그램 (값의 분포를 그래프화)
# 이미지 히스토그램 : 밝기 (또는 색상) 값의 분포를 그래프로 표현 
# 어떤 픽셀이 밝기 0(검정)인지 255(흰색)인지, 각 값이 몇 개나 있는지를 확인
# images : 대상 이미지 리스트 
# channel : 분석할 채널 번호 (B:0, G:1, R:2) grayscale이라면 0으로 쓰면 됨 
# mask : 분석할 영역 마스크(None : 전체) 만약 있다면, 예 : 3 x 3 으로 가리키고 있는 특정 영역만 분석하겠다. 
# histSize : 히스토그램의 빈 개수 
# ranges : 값의 범위 

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])

plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(hist1,color='gray')

# 영상을 컬러로 불러와 3개의 채널을 계산해 히스토그램 그리기 
# 단, 하나의 plot에서 BRG 그래프를 모두 출력 (색상 다르게 표현)

img2 = cv2.imread('./images/candies.png')
# hist_b = cv2.calcHist([img2], [0], None, [256], [0,256])
# hist_g = cv2.calcHist([img2], [1], None, [256], [0,256])
# hist_r = cv2.calcHist([img2], [2], None, [256], [0,256])

colors=['b','g','r']
channels=cv2.split(img2)
plt.subplot(1,2,2)
for ch,color in zip(channels, colors):
    hist = cv2.calcHist([ch],[0],None,[256],[0,255])
    plt.plot(hist, color=color,label=color.upper())
    
    
print('shape',img2.shape)
print('dtype',img2.dtype)

'''
b = img[:,:,0] # blue 계열 (파란 계열을 보면 밝게 보임)
g = img[:,:,1]
r = img[:,:,2]
'''

b, g, r = cv2.split(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

plt.plot(hist1)
plt.show()


# plt.figure(figsize=(8,4))
# plt.plot(hist_b, color='b', label='Blue')
# plt.plot(hist_g, color='g', label='Green')
# plt.plot(hist_r, color='r', label='Red')
# plt.title('Color Histogram')
# plt.xlabel('Pixel value')
# plt.ylabel('Frequency')
# plt.legend()
# plt.tight_layout()
# plt.show()

cv2.waitKey()