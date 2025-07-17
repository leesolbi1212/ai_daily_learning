# 기본 : 인접 리스트로 표현된 그래프의 BFS 순회 

from collections import deque

def bfs_traverse(adj, start):
    """
    adj: {node: [neighbor1, neighbor2, ...], ...}
    start: 탐색 시작 노드
    """
    visited = set([start])
    queue = deque([start])
    order = []  # 방문 순서 기록

    while queue:
        cur = queue.popleft()
        order.append(cur)
        for nbr in adj.get(cur, []):
            if nbr not in visited:
                visited.add(nbr)
                queue.append(nbr)
    return order

# 사용 예
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs_traverse(graph, 'A'))  
# 출력: ['A', 'B', 'C', 'D', 'E', 'F']


# 중급 : 최단 경로 찾기 (무가중치 그래프)
# 큐에 노드를 넣을 때, 해당 노드까지의 거리를 함께 저장하여 시작점에서 다른 모든 노드까지의 최단거리를 구하기

from collections import deque

def bfs_shortest_dist(adj, start):
    """
    adj: 그래프 인접 리스트
    start: 시작 노드
    반환: {node: distance_from_start, ...}
    """
    dist = {start: 0}
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        for nbr in adj.get(cur, []):
            if nbr not in dist:
                dist[nbr] = dist[cur] + 1
                queue.append(nbr)
    return dist

# 사용 예
print(bfs_shortest_dist(graph, 'A'))  
# 출력: {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}

# 심화 : 2D 그리드 (미로)에서 최단 경로 길이 구하기 
# 장애물(값 1)과 이동 가능한 칸(0)이 섞인 격자에서 상하좌우 인접 칸만 이동하여 시작 점에서 목표점까지 최단 거리 (칸 수)를 계산하기 
from collections import deque

def bfs_grid_shortest(grid, start, goal):
    """
    grid: 2D 리스트, 0=이동 가능, 1=장애물
    start, goal: (row, col) 튜플
    반환: 최단 거리 (노드 수; 시작점 포함). 도달 불가 시 -1.
    """
    R, C = len(grid), len(grid[0])
    sr, sc = start
    gr, gc = goal
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return -1

    visited = [[False]*C for _ in range(R)]
    visited[sr][sc] = True
    queue = deque([ (sr, sc, 1) ])  # (행, 열, depth)

    # 상하좌우 이동 벡터
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        r, c, d = queue.popleft()
        if (r, c) == (gr, gc):
            return d
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr, nc, d+1))
    return -1

# 사용 예
maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0],
]
print(bfs_grid_shortest(maze, (0,0), (3,4)))  
# 출력: 9 (최단 경로가 9칸)  

