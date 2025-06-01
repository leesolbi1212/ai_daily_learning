class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    # enqueue: O(1)
    def enqueue(self, data):
        if ((self.rear + 1) % self.size == self.front):
            print("큐가 꽉 찼어요!")
            return
        elif self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    # dequeue: O(1)
    def dequeue(self):
        if self.front == -1:
            print("큐가 비었어요!")
            return None
        removed_data = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed_data

    def display(self):
        if self.front == -1:
            print("큐가 비었어요!")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.display()

cq.dequeue()
cq.display()
