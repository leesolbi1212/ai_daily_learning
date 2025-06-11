def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [64, 25, 12, 22, 11]
bubble_sort(arr)
print("버블 정렬 결과:", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 1) 남은 구간에서 최소값 인덱스 찾기
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 2) 한 번의 swap
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 사용 예
data = [64, 25, 12, 22, 11]
selection_sort(data)
print("정렬 결과:", data)
# 출력 → 정렬 결과: [11, 12, 22, 25, 64]
