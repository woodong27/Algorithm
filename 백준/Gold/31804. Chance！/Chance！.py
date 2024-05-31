# BOJ 31804 G4 Chance!

import sys
from collections import deque


def bfs(start):
    q = deque([[start, 0]])
    visited = [[0, 0] for _ in range(b + 1)]
    visited[start][0] = 1

    while q:
        current, is_chance_used = q.popleft()
        if current == b:
            return visited[current]

        next1, next2 = current + 1, current * 2
        if not is_chance_used:
            next3 = current * 10
            if next3 <= b and not visited[next3][0]:
                visited[next3][1] = visited[current][0] + 1
                q.append([next3, 1])

            if next1 <= b and not visited[next1][0]:
                visited[next1][0] = visited[current][0] + 1
                q.append([next1, 0])

            if next2 <= b and not visited[next2][0]:
                visited[next2][0] = visited[current][0] + 1
                q.append([next2, 0])

        else:
            if next1 <= b and not visited[next1][1]:
                visited[next1][1] = visited[current][1] + 1
                q.append([next1, 1])

            if next2 <= b and not visited[next2][1]:
                visited[next2][1] = visited[current][1] + 1
                q.append([next2, 1])


if __name__ == '__main__':
    enter = sys.stdin.readline
    a, b = map(int, enter().split())

    result = bfs(a)
    answer = max([value for value in result if value]) - 1
    sys.stdout.write(f'{answer}\n')
