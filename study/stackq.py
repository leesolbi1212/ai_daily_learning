class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # enqueue: amortized O(1)
    def enqueue(self, data):
        self.stack1.append(data)

    # dequeue: amortized O(1)
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        return None

sq = StackQueue()
sq.enqueue(1)
sq.enqueue(2)
sq.enqueue(3)

print("스택큐에서 dequeue:", sq.dequeue()) #스택큐에서 dequeue: 1
print("스택큐에서 dequeue:", sq.dequeue()) # 스택큐에서 dequeue: 2
