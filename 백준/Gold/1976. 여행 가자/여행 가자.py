from collections import deque

N=int(input())
M=int(input())
graph=[list(map(int,input().split()))for _ in range(N)]

plan=list(map(int,input().split()))

def search(start,end):
    visited=[start]
    q=deque([start])
    while q:
        current=q.popleft()
        if current==end:
            return 1
        for city in range(len(graph[current])):
            if graph[current][city]==1 and city not in visited:
                q.append(city)
                visited.append(city)

    return 0

ans='YES'
for i in range(len(plan)-1):
    if search(plan[i]-1,plan[i+1]-1)!=1:
        ans='NO'
        break

print(ans)