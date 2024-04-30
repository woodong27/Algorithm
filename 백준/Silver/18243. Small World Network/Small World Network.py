# BOJ 18243 S1 Small World Network

from collections import deque


def bfs(start):
    q = deque([(start, 0)])
    visited = [0] * (n + 1)
    visited[start] = 1
    while q:
        current, depth = q.popleft()
        for node in relations[current]:
            if not visited[node]:
                if depth < 6:
                    visited[node] = 1
                    q.append((node, depth + 1))

    return all(visited[1:])
    

n, k = map(int, input().split())
relations = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

for i in range(1, n + 1):
    result = bfs(i)
    if not result:
        print('Big World!')
        exit(0)

print('Small World!')
