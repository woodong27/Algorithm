def dfs_stack(graph,start):
    visited=[]
    stack=[]
    stack.append(start)

    while stack:
        now=stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])

    return visited

T=int(input())

for x in range(T):
    V,E=map(int,input().split())
    graph=[[]for _ in range(V+1)]
    for i in range(E):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
    S,G=map(int,input().split())

    print(f'#{x+1} {1 if G in dfs_stack(graph,S) else 0}')