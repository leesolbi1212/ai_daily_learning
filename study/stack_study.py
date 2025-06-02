class Stack:
    def __init__(self):
        self.stack = []

    # push : 데이터 추가
    def push(self, item):
        self.stack.append(item)

    # pop : 데이터 삭제 및 반환 (가장 최근 데이터)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    # peek : 가장 최근 데이터 확인 (삭제X)
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None

    # isEmpty : 스택이 비었는지 확인
    def isEmpty(self):
        return len(self.stack) == 0

    # 스택 내용 확인
    def display(self):
        return self.stack

# 사용 예시
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("스택 전체 데이터:", stack.display())
print("pop된 데이터:", stack.pop())
print("가장 최근 데이터:", stack.peek())
print("스택 전체 데이터 (pop 이후):", stack.display())
