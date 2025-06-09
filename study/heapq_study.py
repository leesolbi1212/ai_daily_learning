import heapq

# 빈 리스트로 힙 생성
heap = []

# 데이터 삽입 (자동으로 힙 구조 유지)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)
heapq.heappush(heap, 2)

print("힙 내부 데이터:", heap)

# 가장 작은 값 제거 (pop)
print("가장 작은 값 제거:", heapq.heappop(heap))
print("힙 내부 데이터:", heap)

# 가장 작은 값 조회 (삭제X)
print("가장 작은 값 조회:", heap[0])
