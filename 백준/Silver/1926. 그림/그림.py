# BOJ 1926 S1 그림

import sys

sys.setrecursionlimit(500 ** 2)

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]


def dfs(si, sj):
    global maximum
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < m:
            if not visited[ni][nj] and paper[ni][nj]:
                visited[ni][nj] = 1
                maximum += 1
                dfs(ni, nj)


visited = [[0 for _ in range(m)]for _ in range(n)]
paints = 0
max_value = 0
for i in range(n):
    for j in range(m):
        if paper[i][j] and not visited[i][j]:
            visited[i][j] = 1
            paints += 1
            maximum = 1
            dfs(i, j)
            max_value = max(maximum, max_value)

print(paints)
if not paints:
    max_value = 0
print(max_value)
