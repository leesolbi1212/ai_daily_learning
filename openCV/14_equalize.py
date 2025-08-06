import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./images/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

# 히스토그램 평활화 
# 이미지 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상시키는 기법 
dst1 = cv2.equalizeHist(img1) # 하나의 채널밖에 안됨 (grayscale밖에 안됨)

img2 = cv2.imread('./images/field.bmp')
# YCrCb 색공간 
# Y : 밝기(명도), Cr : 빨강 계열 색상 정보, Cb : 파랑 계열 색상 정보
dst2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
YCrCb = cv2.split(dst2) # 컬러를 3개로 나눔 
YCrCb = list(YCrCb) # 3개 데이터가 들어가 있을 것 
# print(YCrCb)

# 밝기 정보만 가져오면 되니까 0번만 가져오면 됨 
YCrCb[0] = cv2.equalizeHist(YCrCb[0]) # 평활화 시켜준 다음 다시 집어넣어줌
dst2 = cv2.merge(YCrCb) # 다시 합쳐주기 
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR) # YCrCb 색공간을 다시 BGR 색공간으로 변환 (OpenCV 기본 입출력(BGR)에 맞도록 되돌림)

# img1 : 원본 이미지 또는 배열 
# None : 출력 배열(None이면 새로 생성 )
# 0 : 정규화 후 최소값 
# 255 : 정규화 후 최대값 
#  cv2.NORM_MINMAX : 정규화 방식
dst3 = cv2.normalize(img1,None,0,255, cv2.NORM_MINMAX)

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst1], [0], None, [256], [0, 255])
hist3 = cv2.calcHist([dst3], [0], None, [256], [0, 255])


hists = {'hist1': hist1, 'hist2': hist2, 'hist3': hist3}

# 대비가 낮으면 그래프가 이렇게 나옴 -> 평탄화 과정을 거쳐주면 대비가 높아짐
plt.figure(figsize=(10, 6))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(1, 2, i+1)
    plt.title(k)
    plt.plot(v)
# plt.show()

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1) # 높아진 대비 
cv2.imshow('dst2', dst2) # 높아진 대비 

cv2.waitKey()


# split(), merge() -> 명도만 바꿔주고 결과를 봤는데, 이걸 사용하지 않고, 슬라이싱과 인덱싱만을 사용해서 위 예제와 동일하게 결과 영상을 만들어보자. 