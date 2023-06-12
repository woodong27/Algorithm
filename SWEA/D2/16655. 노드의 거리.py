from collections import deque

T=int(input())

def bfs(start,goal,graph):
    que=deque([])
    que.append((start,0))
    visited=[]
    ans=0
    while que:
        node,cnt=que.popleft()
        if node==goal:
            return cnt
        visited.append(node)
        for i in range(V+1):
            if i in graph[node] and i not in visited:
                que.append((i,cnt+1))

    return ans

for tc in range(T):
    V,E=map(int,input().split())
    graph=[[]for _ in range(V+1)]

    for i in range(E):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    S,G=map(int,input().split())

    result=bfs(S,G,graph)
    print(f'#{tc+1} {result}')