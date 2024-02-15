# BOJ 16234 G4 인구 이동

from collections import deque
from copy import deepcopy
from pprint import pprint


def moving(si, sj):
    q = deque([(si, sj)])
    union = [(si, sj)]
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if l <= abs(populations[ni][nj] - populations[ci][cj]) <= r:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    union.append((ni, nj))

    return union


n, l, r = map(int, input().split())

populations = [list(map(int, input().split()))for _ in range(n)]

answer = 0
while True:
    flag = 0
    visited = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                union_country = moving(i, j)

                if len(union_country) > 1:
                    flag = 1
                    union_population = sum(populations[ui][uj] for ui, uj in union_country) // len(union_country)
                    for ui, uj in union_country:
                        populations[ui][uj] = union_population

    if not flag:
        break

    answer += 1

print(answer)
