from collections import deque

T=int(input())

def bfs(start):
    q=deque([start])
    while q:
        current=q.popleft()
        for j in graph[current]:
            if not visited[j]:
                visited[j]=start
                q.append(j)

for tc in range(T):
    N,M=map(int,input().split())
    lst=list(map(int,input().split()))

    graph=[[]for _ in range(N+1)]
    for i in range(0,len(lst),2):
        graph[lst[i]].append(lst[i+1])
        graph[lst[i+1]].append(lst[i])

    visited=[0]*(N+1)
    for i in range(1,N+1):
        if not visited[i]:
            visited[i]=i
            bfs(i)

    visited=set(visited)
    ans=len(visited)-1

    print(f'#{tc+1}', ans)