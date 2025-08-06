# split(), merge() -> 명도만 바꿔주고 결과를 봤는데, 이걸 사용하지 않고, 슬라이싱과 인덱싱만을 사용해서 위 예제와 동일하게 결과 영상을 만들어보자. 

import cv2
import matplotlib.pyplot as plt


img2 = cv2.imread('./images/field.bmp')
dst1 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
dst2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
y = dst1[:,:,0]
cr =  dst1[:,:,1]
cb =  dst1[:,:,2]
y = dst2[:,:,0]
cr =  dst2[:,:,1]
cb =  dst2[:,:,2]
# print(y)

y_eq = cv2.equalizeHist(y)
y_eq_eq = cv2.equalizeHist(y_eq)
dst1[:,:,0] = y_eq
dst2[:,:,0] = y_eq_eq
dst1 = cv2.cvtColor(dst1, cv2.COLOR_YCrCb2BGR)
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)

cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1) #  높아진 대비 
cv2.imshow('dst2', dst2) # 더 높아진 대비 ?
cv2.waitKey()


