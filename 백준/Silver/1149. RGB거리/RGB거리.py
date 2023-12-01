# 1149. RGB 거리

import sys

enter = sys.stdin.readline

N = int(enter())

# Index : 빨강0, 초록1, 파랑2
expenses = [list(map(int, enter().strip().split()))for _ in range(N)]

# dp
# 이전 집의 색깔 중 현재 집 색깔과 다르며 가장 최소인 값을 더해줌
for i in range(1, N):
    expenses[i][0] += min(expenses[i - 1][1], expenses[i - 1][2])
    expenses[i][1] += min(expenses[i - 1][0], expenses[i - 1][2])
    expenses[i][2] += min(expenses[i - 1][0], expenses[i - 1][1])

answer = min(expenses[N - 1])

print(answer)
