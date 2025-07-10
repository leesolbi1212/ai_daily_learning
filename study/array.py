import array, sys

# typecode 'i': signed int, 'f': float, 'd': double
A = array.array('i', [1, 2, 3, 4])
B = array.array('f', (x*0.5 for x in range(6)))

print(A, type(A))  # array('i', [1, 2, 3, 4]) <class 'array.array'>
print(B, type(B))  # array('f', [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]) <class 'array.array'>

# 인덱싱·슬라이싱
print(A[2], A[-1])    # 3, 4
print(A[1:3])         # array('i', [2, 3])

# append, pop
A.append(5)
print(A.pop())        # 5

# 한 번에 여러 요소 추가하기
A.extend([6,7,8])

# 수치 연산 (루프)
# 모든 요소 +1
C = array.array('i', (x+1 for x in A))
print(C) # array('i', [2, 3, 4, 5, 7, 8, 9])

