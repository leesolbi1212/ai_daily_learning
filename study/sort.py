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

def heapify(arr, heap_size, root_index):
    # 최대 힙 속성(부모 ≥ 자식) 복원
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # 왼쪽 자식이 더 크면 갱신
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    # 오른쪽 자식이 더 크면 갱신
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    # 부모가 자식보다 작으면 스왑 후 재귀(heapify 내려가기)
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]
        heapify(arr, heap_size, largest)

def heap_sort(arr):
    n = len(arr)
    # 1) Build Max-Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2) 반복적으로 최대값을 끝으로 보내고 힙 크기 감소
    for i in range(n - 1, 0, -1):
        # 루트(최댓값) ↔ 끝 원소
        arr[0], arr[i] = arr[i], arr[0]
        # 남은 부분을 최대 힙으로 복원
        heapify(arr, i, 0)

# 사용 예
data = [4, 10, 3, 5, 1]
heap_sort(data)
print("힙 정렬 결과:", data)
# 출력 → 힙 정렬 결과: [1, 3, 4, 5, 10]

import random

def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort(arr, lo, p - 1)
        quick_sort(arr, p + 1, hi)

def partition(arr, lo, hi):
    # 피벗으로 마지막 요소 선택
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗을 올바른 위치로
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

# 사용 예
data = [3, 6, 8, 10, 1, 2, 1]
# 랜덤 피벗을 쓰고 싶다면:
# random.shuffle(data)
# pivot = arr[random.randint(lo, hi)]
quick_sort(data)
print("퀵 정렬 결과:", data)
# → 퀵 정렬 결과: [1, 1, 2, 3, 6, 8, 10]

def counting_sort(arr):
    if not arr:
        return arr

    min_val, max_val = min(arr), max(arr)
    k = max_val - min_val + 1

    # 1) 카운트 배열 생성 및 개수 세기
    counts = [0] * k
    for x in arr:
        counts[x - min_val] += 1

    # 2) 누적합 처리
    for i in range(1, k):
        counts[i] += counts[i - 1]

    # 3) 출력 배열에 안정적으로 배치 (뒤쪽부터)
    output = [0] * len(arr)
    for x in reversed(arr):
        idx = x - min_val
        counts[idx] -= 1
        output[counts[idx]] = x

    return output

# 사용 예
data = [4, 2, 2, 8, 3, 3, 1]
sorted_data = counting_sort(data)
print("카운팅 정렬 결과:", sorted_data)
# → 카운팅 정렬 결과: [1, 2, 2, 3, 3, 4, 8]

