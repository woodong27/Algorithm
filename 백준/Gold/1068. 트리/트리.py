# BOJ 1068 G5 트리

import sys


def dfs(start):
    global answer
    if not tree[start]:
        answer += 1
        return
    for node in tree[start]:
        dfs(node)


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    parents = list(map(int, enter().split()))
    delete = int(enter())
    
    tree = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        elif i != delete:
            tree[parents[i]].append(i)
            
    answer = 0
    if delete != root:
        dfs(root)
    
    sys.stdout.write(f'{answer}\n')
