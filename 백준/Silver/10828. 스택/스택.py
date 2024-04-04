# BOJ 10828 S4 스택

import sys

enter = sys.stdin.readline

n = int(enter())

stack = []
for _ in range(n):
    order = enter().strip().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif order[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        print(int(stack == []))
