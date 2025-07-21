def kruskal(n, edges):
    # n: 정점의 개수 (0번부터 n-1번까지 있다고 가정)
    # edges: (u, v, w) 튜플 리스트, u와 v는 연결된 정점 번호, w는 그 간선의 가중치

    # 1) 유니온-파인드(Disjoint Set) 구조를 위한 부모 배열 초기화
    parent = list(range(n))  
    #    parent[i] = i 로 설정 → 처음에는 모든 정점이 각자 다른 집합의 대표(루트)

    # 2) find 함수: x가 속한 집합의 대표(루트)를 찾고 경로 압축
    def find(x):
        # 만약 parent[x]가 자기 자신이 아니면, 재귀적으로 루트까지 올라가서
        # 최종 루트를 parent[x]에 직접 연결(path compression)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    # 3) union 함수: a와 b를 같은 집합으로 합치되, 사이클이 생기지 않을 때만 합침
    def union(a, b):
        ra = find(a)  # a의 루트 찾기
        rb = find(b)  # b의 루트 찾기
        if ra != rb:
            # 두 루트가 다르면 서로 다른 집합이므로 합친다
            parent[rb] = ra
            return True   # 합치기에 성공(사이클 없음)
        return False      # ra == rb 이면 이미 같은 집합, 사이클 방지 차원에서 합치지 않음

    # 4) MST(최소 신장 트리) 비용과 포함된 간선 개수를 저장할 변수
    mst_cost = 0    # MST에 포함된 간선들의 가중치 합
    edge_count = 0  # MST에 포함된 간선 개수

    # 5) 모든 간선을 가중치 오름차순으로 정렬한 다음 하나씩 꺼내서 처리
    for u, v, w in sorted(edges, key=lambda x: x[2]):
        # sorted(..., key=lambda x: x[2]) → 각 튜플의 3번째 항목(w)을 기준으로 정렬
        if union(u, v):
            # 사이클이 생기지 않는다면(두 정점이 다른 집합에 속해 있었다면)
            mst_cost += w        # 이 간선의 가중치를 MST 비용에 더하기
            edge_count += 1      # 포함된 간선 개수 1 증가
            if edge_count == n - 1:
                # n개 정점을 모두 연결하려면 n-1개의 간선만 필요 → 다 뽑았으면 종료
                break

    return mst_cost  # 계산된 최소 신장 트리의 총 가중치 반환
