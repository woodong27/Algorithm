# BOJ 28066 S2 타노스는 유세푸스가 밉다

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().strip().split())

squirrels = deque([i for i in range(1, n + 1)])

while True:
    if len(squirrels) < k:
        print(squirrels[0])
        break
    else:
        first = squirrels.popleft()
        temp = []
        while True:
            if len(temp) >= k - 1:
                break
            temp.append(squirrels.popleft())
        squirrels.append(first)
