# BOJ 1238 G3 파티

import sys
from heapq import heappush, heappop


def dijkstra(start, graph):
    q = []
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heappush(q, [0, start])
    while q:
        weight, current = heappop(q)
        if distance[current] >= weight:
            for next_, weight_ in graph[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, [weight + weight_, next_])

    return distance[1:]


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m, x = map(int, enter().strip().split())
    villages = [[] for _ in range(n + 1)]
    reverse = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, enter().strip().split())
        villages[a].append([b, c])
        reverse[b].append([a, c])

    from_x = dijkstra(x, villages)
    to_x = dijkstra(x, reverse)

    answer = max([value1 + value2 for value1, value2 in zip(from_x, to_x)])
    print(answer)
