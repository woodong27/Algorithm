# BOJ 2573 G4 빙산

from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]


# 빙하가 1년 마다 녹는다.
def melting():
    melting_amount = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if sea[i][j]:
                count = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < n and 0 <= nj < m and not sea[ni][nj]:
                        count += 1
                melting_amount[i][j] = count

    for i in range(n):
        for j in range(m):
            if sea[i][j]:
                if sea[i][j] < melting_amount[i][j]:
                    sea[i][j] = 0
                else:
                    sea[i][j] -= melting_amount[i][j]


# 덩어리 계산
def count_iceberg():
    global flag1, flag2
    visited = [[0 for _ in range(m)]for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(m):
            if sea[i][j] and not visited[i][j]:
                temp += 1
                visited[i][j] = 1
                q = deque([(i, j)])
                while q:
                    ci, cj = q.popleft()
                    for k in range(4):
                        ni, nj = ci + di[k], cj + dj[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            if not visited[ni][nj] and sea[ni][nj]:
                                q.append((ni, nj))
                                visited[ni][nj] = 1

            if temp > 1:
                flag1 = 1
                break

    if not temp:
        flag2 = 1

    return visited


n, m = map(int, input().split())

sea = [list(map(int, input().split()))for _ in range(n)]

# 빙하가 두 덩어리 이상으로 쪼개졌다면 flag1에 해당
flag1 = 0
# 빙하가 여러 덩어리로 쪼개지기 전에 다 녹아버렸다면 flag2에 해당
flag2 = 0
answer = 0
while True:
    answer += 1
    melting()
    result = count_iceberg()

    if flag1 or flag2:
        break

if flag2:
    answer = 0
print(answer)
