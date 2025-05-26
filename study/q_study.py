# 리스트를 이용한 큐
queue_list = []

# enqueue: 큐에 넣기
queue_list.append(1)
queue_list.append(2)
queue_list.append(3)
print("enqueue 후 리스트 큐:", queue_list)

# dequeue: 큐에서 빼기
queue_list.pop(0)  # 큐의 맨 앞에서 빼기 (느림 O(n))
print("dequeue 후 리스트 큐:", queue_list)
