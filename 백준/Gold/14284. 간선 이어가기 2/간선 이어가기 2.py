# BOJ 14284 G5 간선 이어가기 2

from heapq import heappush, heappop


def dijkstra(start, end):
    q = []
    distance = [float('inf')] * (n + 1)
    heappush(q, (0, start))
    while q:
        weight, current = heappop(q)
        if current == end:
            return distance[end]

        if distance[current] >= weight:
            for node, weight_ in graph[current]:
                if weight + weight_ < distance[node]:
                    distance[node] = weight + weight_
                    heappush(q, (weight + weight_, node))


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])
        graph[b].append([a, c])

    s, t = map(int, input().split())

    answer = dijkstra(s, t)
    print(answer)
