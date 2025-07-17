def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# 사용 예
numbers = [4, 2, 7, 1, 9]
print(linear_search(numbers, 7))   # 출력: 2
print(linear_search(numbers, 5))   # 출력: -1
