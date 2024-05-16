# BOJ 1865 G3 웜폴

import sys


def bellman_ford(start):
    distance = [float('inf')] * n
    distance[start] = 0

    for _ in range(n-1):
        is_updated = False
        for i in range(n):
            for node, weight in points[i]:
                if distance[i] + weight < distance[node]:
                    distance[node] = distance[i] + weight
                    is_updated = True
                    
        if not is_updated:
            break

    for i in range(n):
        for node, weight in points[i]:
            if distance[i] + weight < distance[node]:
                return True

    return False


if __name__ == '__main__':
    enter = sys.stdin.readline
    tc = int(enter())
    for _ in range(tc):
        n, m, w = map(int, enter().strip().split())
        points = [[] for _ in range(n)]
        for __ in range(m):
            s, e, t = map(int, enter().strip().split())
            points[s-1].append([e-1, t])
            points[e-1].append([s-1, t])

        for ___ in range(w):
            s, e, t = map(int, enter().strip().split())
            points[s-1].append([e-1, -t])

        answer = 'NO'
        for i in range(n):
            if bellman_ford(i):
                answer = 'YES'
                break

        print(answer)
