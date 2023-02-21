from collections import deque

queue=deque([])
visited=[]

def BFS(start):
    queue.append(start)

    while queue:
        node=queue.popleft()
        visited.append(node)
        for i in range(1,V+1):
            if graph[node][i]==1 and i not in visited:
                queue.append(i)


V,E=map(int,input().split())
graph=[[0 for _ in range(V+1)]for _ in range(V+1)]

for i in range(E):
    v1,v2=map(int,input().split())
    graph[v1][v2]=1 #인접행렬

BFS(1)
print(visited)
