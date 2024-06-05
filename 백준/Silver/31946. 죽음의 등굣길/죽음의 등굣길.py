# BOJ 31946 S1 죽음의 등굣길

from collections import deque
import sys


def check(si, sj, ei, ej):
    if abs(si - ei) + abs(sj - ej) <= x:
        return True
    return False


def bfs():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0, load[0][0])])
    while q:
        ci, cj, color = q.popleft()
        if ci == n - 1 and cj == m - 1:
            return 'ALIVE'
        for i in range(n):
            for j in range(m):
                if load[i][j] == color and not visited[i][j] and check(ci, cj, i, j):
                    q.append((i, j, color))
                    visited[i][j] = 1

    return 'DEAD'


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    m = int(enter())
    load = [list(map(int, enter().split())) for _ in range(n)]
    x = int(enter())

    answer = bfs()
    sys.stdout.write(f'{answer}\n')
