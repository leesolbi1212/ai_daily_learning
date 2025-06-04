class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        """리스트 끝에 새 노드 추가"""
        new_node = Node(val)
        if not self.head:
            # 빈 리스트: 새 노드가 자기 자신을 가리키도록
            self.head = new_node
            new_node.next = new_node
        else:
            # 마지막 노드를 찾아서 그 다음에 새 노드 연결
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self, val):
        """리스트 처음(헤드 위치)에 새 노드 추가"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            # 헤드를 끼워넣고, 마지막 노드가 새 헤드를 가리키게
            cur = self.head
            while cur.next is not self.head:
                cur = cur.next
            new_node.next = self.head
            cur.next = new_node
            self.head = new_node

    def delete(self, val):
        """값이 val인 노드 삭제(첫 번째 발견)"""
        if not self.head:
            return False
        cur = self.head
        prev = None
        while True:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    # 헤드를 삭제하는 경우
                    # 마지막 노드 찾아서 새 헤드를 가리키게
                    tail = self.head
                    while tail.next is not self.head:
                        tail = tail.next
                    # 리스트가 노드 하나 뿐인 경우
                    if tail is self.head:
                        self.head = None
                        return True
                    tail.next = cur.next
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
            if cur is self.head:
                break
        return False  # 찾지 못함

    def traverse(self):
        """값들을 순환하며 리스트 형태로 반환"""
        items = []
        if not self.head:
            return items
        cur = self.head
        while True:
            items.append(cur.val)
            cur = cur.next
            if cur is self.head:
                break
        return items

# === 사용 예시 ===
if __name__ == "__main__":
    cll = CircularLinkedList()
    # append
    for x in [10, 20, 30]:
        cll.append(x)
    print("append 후:", cll.traverse())  
    # prepend
    cll.prepend(5)
    print("prepend 후:", cll.traverse())
    # delete 중간 노드
    cll.delete(20)
    print("20 삭제 후:", cll.traverse())
    # delete 헤드
    cll.delete(5)
    print("5(헤드) 삭제 후:", cll.traverse())
    # delete 존재하지 않는 값
    removed = cll.delete(999)
    print("999 삭제 시도:", removed, "→", cll.traverse())
