# BOJ 13023 G5 ABCDE

n, m = map(int, input().split())
relations = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(start, friends):
    global answer
    if len(friends) == 5:
        answer = 1
        return

    for node in relations[start]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, friends + [node])
            visited[node] = 0


answer = 0
visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, [i])
    visited[i] = 0
    if answer:
        break

print(answer)
