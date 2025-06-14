# 리스트를 이용한 큐
queue_list = []

# enqueue: 큐에 넣기
queue_list.append(1)
queue_list.append(2)
queue_list.append(3)
print("enqueue 후 리스트 큐:", queue_list) #enqueue 후 리스트 큐: [1, 2, 3]

# dequeue: 큐에서 빼기
queue_list.pop(0)  # 큐의 맨 앞에서 빼기 (느림 O(n))
print("dequeue 후 리스트 큐:", queue_list) #dequeue 후 리스트 큐: [2, 3]

# collections.deque 사용

from collections import deque

# deque 큐 생성
queue_deque = deque()

# enqueue: O(1)
queue_deque.append(1)
queue_deque.append(2)
queue_deque.append(3)
print("enqueue 후 deque 큐:", queue_deque) #enqueue 후 deque 큐: deque([1, 2, 3])

# dequeue: O(1)
queue_deque.popleft()
print("dequeue 후 deque 큐:", queue_deque) #dequeue 후 deque 큐: deque([2, 3])
