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

for x in range(10):
    S,G=0,99
    tc,N=map(int,input().split())
    lst=list(map(int,input().split()))
    v1=[]
    v2=[]
    for i in range(N*2):
        if i%2:
            v2.append(lst[i])
        else:
            v1.append(lst[i])

    graph=[[]for _ in range(100)]
    for i in range(N):
        graph[v1[i]].append(v2[i])

    print(f'#{tc} {1 if G in dfs_stack(graph,S) else 0}')