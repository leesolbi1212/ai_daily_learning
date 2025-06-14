class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    # 간단한 해시 함수 (key를 인덱스로 변환)
    def _hash(self, key):
        return hash(key) % self.size
    
    # 데이터 삽입
    def set(self, key, value):
        index = self._hash(key)
        # 같은 키가 존재하면 업데이트
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    # 데이터 조회
    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None
    
    # 데이터 삭제
    def remove(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                self.table[index].pop(i)
                return True
        return False

    # 전체 테이블 출력
    def display(self):
        return self.table

# 사용 예시
hash_table = HashTable(10)
hash_table.set('name', '솔비')
hash_table.set('age', 25)
hash_table.set('city', 'Seoul')

print("name:", hash_table.get('name'))
print("전체 해시테이블:", hash_table.display())

hash_table.remove('age')
print("삭제 후 해시테이블:", hash_table.display())
