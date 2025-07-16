# 시간복잡도 문제 

# 1 
def example(lst):
    print(lst[0])
# O(1)
# 이 함수는 리스트 lst의 첫 번째 요소를 출력함. 리스트에서 한 번의 접근만 하므로 실행 시간은 입력 크기와 무관하게 항상 일정하다. 

# 2 
def example2(lst):
    for item in lst:
        print(item)
# O(n)
# 리스트 lst의 모든 요소를 한 번씩 출력함. 리스트의 길이에 비례하여 반복하므로(향상된 for문) 실행 시간은 입력크기 n에 비례함. 

# 3
def example3(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
# O(log n)
# 1부터 시작해서 i를 2배씩 증가시키며 n보다 작을 때까지 출력함. i의 값이 지수적(매 반복마다 같은 배율, 기하급수적으로)으로 증가하므로 실행 시간은 입력 크기 n에 대해 로그 함수(지수적 증가의 반복 횟수를 역으로 생각하기)의 비율로 증가함. 
# n에 도달하기까지 배율을 몇 번 곱해야하는지를 나타내며, 그 횟수가 log(n)에 비례한다.

# 4
def example4(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(i,j)
# O(n^2)
# lst의 모든 요소를 쌍으로 출력함. 이중 반복문을 사용하여 모든 요소를 비교하므로 실행 시간은 입력 크기 n에 대해 제곱 비율로 증가함. 

# 5
def example5(n):
    if n <=1:
        return 1 
    else :
        return n * example5(n-1)
# O(n!)
# 팩토리얼 계산하는 재귀함수, 모든 가능한 순열의 수를 계산함. 실행 시간은 입력 크기 n에 대해 팩토리얼 비율로 급격히 증가함 

# 6
def example6(lst):
    lst.sort()
    for item in lst:
        print(item)
# O(n log n)
# lst를 정렬한 후 모든 요소를 출력. 정렬 알고리즘의 시간 복잡도가 O(n log n) 이므로 전체 시간복잡도도 동일 















for i in range(1, 3+1): #행을 만드는 역할, 반복이 한 번 끝날때마다 한 줄이 새로 생김 
    for ii in range(i): #열(별의 개수)을 만드는 역할을 함. 각 행에 몇 개의 별을 찍을지 결정
        print('*',end='')
    print()
