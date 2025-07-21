import heapq #작은 수를 빠르게 꺼내주는 파이썬 기본 라이브러리 
# “가장 짧은 거리”부터 처리하려고 최소 힙(min‑heap)을 쓸 예정 

def dijkstra_heap(n, adj, start):
    INF = float('inf') # 아직 거리를 모를 때 무한대라고 표시하기 위해 inf를 쓴다.
    dist = [INF] * (n + 1) # 각 정점까지의 최단거리 기록판 (처음엔 모두 무한대로 설정 아직 도달 못했음)
    dist[start] = 0 # 출발점(start)까지 거리는 0이니까 0으로 채움 
    heap = [(0, start)]  # (거리, 정점)

    while heap:
        cur_d, u = heapq.heappop(heap) # 가장 작은 거리를 꺼내준다. (cur_d), u : 정점 번호 
        if cur_d > dist[u]:
            continue    # 이미 더 짧은 경로 처리된 적 있으면 건너뛰기 

        for v, w in adj[u]: # 정점 u에 붙어있는 모든 이웃(v)와 그 간선의 가중치(w) 목록을 가져온다.
            nd = cur_d + w # “지금까지 온 거리(cur_d)” + “u→v 가중치(w)” → 새로운 거리(nd).
            if nd < dist[v]: # 기록판에 적힌 이전 거리보다 작으면 더 짧은 길을 찾은 것 
                dist[v] = nd # 최단 거리 기록판 갱신 
                heapq.heappush(heap, (nd, v)) # 힙에 새 거리를 넣어서 다음 번에 더 짧은 거리부터 꺼내 처리하도록 예약.

    return dist


    
    # 모든 정점을 돌면서 더 짧은 길을 찾고 힙이 빌 때까지 반복햇으니 최종적으로는 dist[i]에는 시작점에서
    # i번 정점까지의 최단거리가 정확히 들어있다.
    
    # ── 예제 사용 ──
n = 4
adj = [[] for _ in range(n+1)]
# (양방향 그래프라고 가정)
edges = [
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 2),
    (2, 4, 5),
    (3, 4, 1),
]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

start = 1
distances = dijkstra_heap(n, adj, start)

# 출력
# 1번에서 각 정점까지 최단 거리: [inf, 0, 1, 3, 4]
print(distances)