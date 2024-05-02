# BOJ 18352 S2 특정 거리의 도시 찾기

import heapq
import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])

distance = [float('inf')] * (n + 1)
q = []
heapq.heappush(q, (0, x))
distance[x] = 0

while q:
    weight, current = heapq.heappop(q)

    if distance[current] >= weight:
        for node_, weight_ in graph[current]:
            if weight + weight_ < distance[node_]:
                distance[node_] = weight + weight_
                heapq.heappush(q, (weight + weight_, node_))

result = [index for index, value in enumerate(distance) if value == k]

if not result:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')
