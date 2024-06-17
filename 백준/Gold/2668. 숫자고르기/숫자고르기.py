# BOJ 2668 G5 숫자고르기

import sys
sys.setrecursionlimit(10000)


def dfs(start):
    global visited, finished, result
    stack = []
    current = start
    while True:
        if not visited[current]:
            visited[current] = 1
            stack.append(current)
            current = number[current]
        elif visited[current] and not finished[current]:
            if current in stack:
                start = stack.index(current)
                result.update(stack[start:])
            break
        else:
            break

    while stack:
        finished[stack.pop()] = 1


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    number = [0] + [int(enter()) for _ in range(n)]

    visited = [0] * (n + 1)
    finished = [0] * (n + 1)
    result = set()

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    result = sorted(result)
    sys.stdout.write(f'{len(result)}\n')
    for num in result:
        sys.stdout.write(f'{num}\n')
