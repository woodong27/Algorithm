# BOJ 1967 G4 트리의 지름

import sys


def dfs(current):
    global visited

    for next_, weight_ in tree[current]:
        if visited[next_] == -1:
            visited[next_] = visited[current] + weight_
            dfs(next_)


if __name__ == '__main__':
    sys.setrecursionlimit(10_000 ** 2)
    enter = sys.stdin.readline

    n = int(enter())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, enter().split())
        tree[a].append([b, c])
        tree[b].append([a, c])

    visited = [-1] * (n + 1)
    visited[1] = 0
    dfs(1)

    start = visited.index(max(visited))
    visited = [-1] * (n + 1)
    visited[start] = 0
    dfs(start)

    answer = max(visited)
    sys.stdout.write(f'{answer}\n')
