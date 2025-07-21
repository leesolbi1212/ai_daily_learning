n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 주어진 일들의 시작/종료 시간이 겹치지 않도록 최대 개수 선택
activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11)]
# 종료 시간을 기준으로 오름차순 정렬
activities.sort(key=lambda x: x[1])

selected = []
current_end = 0
for start, end in activities:
    if start >= current_end:
        selected.append((start, end))
        current_end = end

print("선택한 활동:", selected)
# 결과: [(1,4),(5,7),(8,11)] 총 3개
