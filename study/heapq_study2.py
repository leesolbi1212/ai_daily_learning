import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))  # 우선순위로 정렬되어 저장됨

    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)[1]  # 우선순위 높은 순서로 반환
        else:
            return None

    def isEmpty(self):
        return len(self.queue) == 0

# 사용 예시
pq = PriorityQueue()
pq.enqueue('Low Priority Task', 3)
pq.enqueue('High Priority Task', 1)
pq.enqueue('Medium Priority Task', 2)

print(pq.dequeue())  # High Priority Task
print(pq.dequeue())  # Medium Priority Task
print(pq.dequeue())  # Low Priority Task