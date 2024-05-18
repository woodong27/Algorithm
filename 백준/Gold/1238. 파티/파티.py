# BOJ 1238 G3 파티

from heapq import heappush, heappop


def dijkstra(start, **kwargs):
    end = kwargs.get('end', False)

    q = []
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heappush(q, [0, start])
    while q:
        weight, current = heappop(q)
        if end and current == end:
            return distance[end]

        if distance[current] >= weight:
            for next_, weight_ in villages[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, [weight + weight_, next_])

    return distance


if __name__ == '__main__':
    n, m, x = map(int, input().split())
    villages = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        villages[a].append([b, c])

    from_x = dijkstra(x)
    answer = 0
    for i in range(1, n + 1):
        result = dijkstra(i, end=x)
        answer = max(answer, from_x[i] + result)

    print(answer)
