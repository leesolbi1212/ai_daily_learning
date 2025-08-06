import cv2

# 두 영상 합쳐보기 
cap1 = cv2.VideoCapture('./movies/35427-407130886_tiny.mp4')
cap2 = cv2.VideoCapture('./movies/money.mp4')

# 조건 : 해상도가 같아야 함 

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)
frame_cnt2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps2 = int(cap2.get(cv2.CAP_PROP_FPS))

print(w,h,frame_cnt1,frame_cnt2,fps1,fps2)

# fourcc(*'DIVX') : .avi 를 말하는 것. 압축 기술을 적으면 된다. 
fourcc = cv2.VideoWriter.fourcc(*'DIVX')
out = cv2.VideoWriter('mix.avi', fourcc, fps1, (w, h))

for i in range(frame_cnt1):
    ret, frame = cap1.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10)==27:
        break
    
for i in range(frame_cnt2):
    ret, frame = cap2.read()
    cv2.imshow('output',frame)
    out.write(frame)
    if cv2.waitKey(10)==27:
        break
    
cap1.release()
cap2.release()
out.release()