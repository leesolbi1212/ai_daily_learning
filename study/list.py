# 기본 생성 및 접근 
L1 = []  
L2 = list()  
L3 = [1, 2, 3, 'four', [5,6]]

print(L3[0])      # 1
print(L3[-1])     # [5,6]
print(L3[1:4])    # [2, 3, 'four']

# 주요 메서드 사용
L = [10, 20, 30]
L.append(40)              # [10,20,30,40]
L.insert(2, 25)           # [10,20,25,30,40]
L.extend([50, 60])        # [10,20,25,30,40,50,60]
print(L.pop())            # 60, L은 끝 요소 제거
print(L.pop(1))           # 20, 인덱스 1 제거
print(L.remove(25))       # 값으로 제거
print(L.index(30))        # 2
print(L.count(10))        # 1

# 리스트 컴프리헨션 & 제너레이터 
# 단순 컴프리헨션
squares = [x*x for x in range(10)]
# 조건부 컴프리헨션
even_squares = [x*x for x in range(10) if x % 2 == 0]

# 중첩 컴프리헨션 (2차원 리스트 평탄화)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]

# 제너레이터 표현식 (메모리 절약)
gen = (x*x for x in range(10))
for v in gen:
    print(v, end=' ')