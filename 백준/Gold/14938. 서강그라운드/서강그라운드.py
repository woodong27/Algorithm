# BOJ 14938 G4 서강그라운드

import heapq

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [float('inf')] * (n + 1)
    distance[start] = 0

    while q:
        weight, current = heapq.heappop(q)

        if distance[current] >= weight:
            for node, weight_ in graph[current]:
                if weight + weight_ < distance[node]:
                    distance[node] = weight + weight_
                    heapq.heappush(q, (weight + weight_, node))

    return [index for index, value in enumerate(distance) if value <= m]


answer = 0
for i in range(1, n + 1):
    result = dijkstra(i)
    answer = max(answer, sum([item[idx] for idx in result]))

print(answer)
