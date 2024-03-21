# BOJ 1240 G5 노드사이의 거리

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2, distance = map(int, input().split())
    tree[node1].append((node2, distance))
    tree[node2].append((node1, distance))


def dfs(s, e, count):
    if s == e:
        print(count)
    for node, distance in tree[s]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, e, count + distance)


for _ in range(m):
    start, end = map(int, input().split())
    visited = [0] * (n + 1)
    visited[start] = 1
    dfs(start, end, 0)
