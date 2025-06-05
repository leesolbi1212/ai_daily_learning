# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 이진 트리 클래스 정의
class BinaryTree:
    def __init__(self):
        self.root = None
    
    # 데이터 삽입 (레벨 순서대로 채우기)
    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)
            
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    # 레벨순회 (Level-order Traversal)로 데이터 출력
    def level_order(self):
        result = []
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

# 사용 예시
bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)

print("레벨 순회 결과:", bt.level_order())
