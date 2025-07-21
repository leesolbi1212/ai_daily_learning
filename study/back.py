def solve_n_queens(n):
    cols = set()
    diag1 = set()  # r+c
    diag2 = set()  # r-c
    board = []
    result = []

    def dfs(r):
        if r == n:
            result.append(board[:])
            return
        for c in range(n):
            if c in cols or (r+c) in diag1 or (r-c) in diag2:
                continue
            cols.add(c); diag1.add(r+c); diag2.add(r-c)
            board.append(c)      # row r에 col c에 퀸 배치
            dfs(r+1)
            board.pop()          # 되돌아가기
            cols.remove(c); diag1.remove(r+c); diag2.remove(r-c)

    dfs(0)
    return result

print(len(solve_n_queens(8)))  # 92가지 해

def subset_sum(arr, target):
    result = []
    path = []

    def dfs(idx, s):
        if s == target:
            result.append(path[:])
            return
        if s > target or idx == len(arr):
            return
        # 1) 선택
        path.append(arr[idx])
        dfs(idx+1, s+arr[idx])
        path.pop()  # 되돌아가기
        # 2) 비선택
        dfs(idx+1, s)

    dfs(0, 0)
    return result

print(subset_sum([2,3,6,7], 7))  # [[7], [2,3,2] 등]
