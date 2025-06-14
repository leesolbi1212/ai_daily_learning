# 연결 리스트의 노드 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 큐 정의 (연결 리스트 기반)
class LinkedListQueue:
    def __init__(self):
        self.head = None  # 맨 앞 노드
        self.tail = None  # 맨 뒤 노드

    # enqueue: O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # dequeue: O(1)
    def dequeue(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_data

queue_linked = LinkedListQueue()
queue_linked.enqueue(1)
queue_linked.enqueue(2)
queue_linked.enqueue(3)

print("enqueue 후 연결리스트 큐:")
node = queue_linked.head
while node:
    print(node.data, end=" -> ")
    node = node.next
    
# enqueue 후 연결리스트 큐:
# 1 -> 2 -> 3 -> 

queue_linked.dequeue()
print("\ndequeue 후 연결리스트 큐:")
node = queue_linked.head
while node:
    print(node.data, end=" -> ")
    node = node.next
    
# dequeue 후 연결리스트 큐:
# 2 -> 3 ->
