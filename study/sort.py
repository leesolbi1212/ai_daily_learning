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
print("선택 정렬 결과:", data)
# 출력 → 정렬 결과: [11, 12, 22, 25, 64]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]         # 삽입할 값
        j = i - 1
        # 정렬된 구간에서 key보다 큰 요소를 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # 빈 자리에 key 삽입
        arr[j + 1] = key

# 사용 예
data = [12, 11, 13, 5, 6]
insertion_sort(data)
print("삽입 정렬 결과:", data)
# → 정렬 결과: [5, 6, 11, 12, 13]

def merge_sort(arr):
    # 1) 분할: 길이 1 이하이면 그대로 반환
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])     # 왼쪽 절반 정렬
    right = merge_sort(arr[mid:])    # 오른쪽 절반 정렬

    # 2) 병합 단계
    merged = []
    i = j = 0
    # 양쪽 리스트를 한 칸씩 비교하며 작은 값을 merged에 추가
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 남은 요소가 있다면 뒤에 덧붙임
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# 사용 예
data = [38, 27, 43, 3, 9, 82, 10]
sorted_data = merge_sort(data)
print("병합 정렬 결과:", sorted_data)
# 병합 정렬 결과: [3, 9, 10, 27, 38, 43, 82]
