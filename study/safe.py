from queue import Queue

# 스레드 안전 큐 생성
q = Queue()

# enqueue (스레드 안전)
q.put(1)
q.put(2)
q.put(3)

print("queue.Queue에서 dequeue:", q.get())
print("queue.Queue에서 dequeue:", q.get())