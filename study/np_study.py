# 생성 방식 

import numpy as np

# 1D
v1 = np.array([1,2,3,4], dtype=np.int32)
# 2D
M = np.arange(12).reshape(3,4)
# zeros, ones, eye, linspace
z = np.zeros((2,3))
o = np.ones((2,2))
I = np.eye(3)
lin = np.linspace(0, 1, 5)  # [0.,0.25,0.5,0.75,1.]

# 인덱싱, 슬라이싱 

# 기본 슬라이스
print(M[1,2])        # 6 → M의 (1,2) 위치 값
print(M[:,0])        # [0 4 8] → 첫 번째 열 전체
print(M[0:2, 1:3])   # [[1 2] [5 6]] → 부분 행렬 (0~1행, 1~2열)

# 불린 인덱싱
mask = (M % 2 == 0) # 짝수만 
print(M[mask])       # [ 0  2  4  6  8 10] → M에서 짝수만 선택한 결과

# 팬시 인덱싱
rows = np.array([0,2])
cols = np.array([1,3])
print(M[rows, cols]) # [ 1 11] → M[0,1]과 M[2,3]의 값

# 벡터화 & 브로드캐스트 

# 스칼라 연산
print(v1 + 10) # [11 12 13 14] → v1의 모든 요소에 10을 더한 결과

# 배열 간 연산
v2 = np.arange(4)
print(v1 * v2) # [ 0  2  6 12] → v1과 v2의 요소별 곱셈 결과

# 브로드캐스트 예
A = np.ones((3,1))
B = np.arange(3)     # shape (3,)
print(A + B)         # [[1. 2. 3.]
                     #  [1. 2. 3.]
                     #  [1. 2. 3.]] → 브로드캐스팅으로 인한 배열 연산 결과
# 통계 함수
print(M.mean(), M.mean(axis=0), M.std(axis=1))
# 5.5 (전체 평균)
# [4. 5. 6. 7.] (각 열의 평균)
# [1.11803399 1.11803399 1.11803399] (각 행의 표준편차)

# 선형대수
print(np.dot(v1, v2))        # 20 → v1과 v2의 내적 결과
print(np.linalg.inv(I))      # [[1. 0. 0.]
                             #  [0. 1. 0.]
                             #  [0. 0. 1.]] → 단위 행렬(I)의 역행렬 (단위행렬은 역행렬이 자기 자신)


# 변경 & 복사
M2 = M.copy()
M3 = M.flatten()             # 평탄화

# 성능 비교해보기 

import timeit
N = 10**7

# Python list 루프
t1 = timeit.timeit("L=[i for i in range(N)]; [x+1 for x in L]", globals=globals(), number=3)

# NumPy 벡터화
setup = "import numpy as np; A = np.arange(N)"
t2 = timeit.timeit("A+1", setup=setup, globals={'N':N}, number=3)

print(f"list loop: {t1:.3f}s") # list loop: 5.007s
print(f"numpy vec: {t2:.3f}s") # numpy vec: 0.092s

