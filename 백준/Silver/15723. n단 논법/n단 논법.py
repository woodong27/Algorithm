# BOJ 15723 S1 n단 논법

from collections import deque


def bfs(start, end):
    visited = [start]
    q = deque([start])
    while q:
        current = q.popleft()
        if current == end:
            print('T')
            return
        if current in premises.keys():
            for letter in premises[current]:
                if letter not in visited:
                    visited.append(letter)
                    q.append(letter)

    print('F')


n = int(input())

premises = {}
for _ in range(n):
    a, is_, b = input().split()
    if a not in premises.keys():
        premises[a] = [b]
    else:
        premises[a].append(b)


m = int(input())
for _ in range(m):
    a, is_, b = input().split()
    bfs(a, b)
