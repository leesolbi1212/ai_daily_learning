import heapq  # 파이썬 기본 제공 최소 힙 모듈

def prim(n, adj, start=0):
    """
    n: 정점 개수 (0번부터 n-1번 정점)
    adj: 인접 리스트. adj[u] = [(v, w_uv), ...] 형식으로
         u 정점에 연결된 이웃 정점 v와 가중치 w_uv 리스트
    start: MST 시작할 출발 정점 (기본값 0번)
    """
    # 1) 각 정점이 MST에 포함되었는지 표시하는 방문표
    visited = [False] * n  
    #    처음엔 모두 False → 아직 어떤 정점도 MST에 추가되지 않음

    # 2) 힙(우선순위 큐) 초기화: (간선 가중치, 정점) 튜플을 담음
    #    시작점은 가중치 0으로 “MST에 가장 먼저 추가될 후보”로 넣어둠
    hq = [(0, start)]     # 처음 꺼낼 때 w=0, u=start

    # 3) MST 전체 가중치 합을 저장할 변수
    mst_cost = 0

    # 4) 힙이 빌 때까지 반복 → 모든 정점이 MST에 추가될 때까지
    while hq:
        w, u = heapq.heappop(hq)  
        #    힙에서 가장 작은 가중치 w를 가진 (w, u) 꺼내기
        #    이게 “지금까지 발견된 가장 짧은 간선” 후보

        # 5) 이미 방문(추가)된 정점이면 무시하고 다음으로
        if visited[u]:
            continue

        # 6) 방문 표시 → u 정점을 MST에 추가
        visited[u] = True

        # 7) MST 비용에 이 간선 가중치 더하기
        #    (start 정점의 첫 w=0은 MST에 첫 노드만 추가하는 역할)
        mst_cost += w

        # 8) u 정점과 연결된 모든 간선을 검사
        for v, w_uv in adj[u]:
            #    v: 이웃 정점, w_uv: u→v 간선 가중치
            if not visited[v]:
                #    아직 MST에 추가되지 않은 정점 v에 대해
                #    “u→v 간선”을 후보로 힙에 넣기
                heapq.heappush(hq, (w_uv, v))

    # 9) 모든 정점이 MST에 포함되면 최종 총 가중치 반환
    return mst_cost
