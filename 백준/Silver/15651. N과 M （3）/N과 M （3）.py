# BOJ 15651 S3 N과 M (3)

import sys


def backtrack(current, idx):
    global visited
    if len(current) == m:
        print(*current)
        visited[idx] = 0
        return

    for j in range(1, n + 1):
        if not visited[j]:
            next_ = current + [j]
            if len(next_) == m:
                visited[j] = 1
            backtrack(current + [j], j)


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())

    visited = [0] * (n + 1)
    for i in range(1, n + 1):
        backtrack([i], i)
