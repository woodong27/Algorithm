from collections import deque

def BFS(start):
    que=deque([])
    que.append((start,0))
    path=[]
    while que:
        node,cnt=que.popleft()
        if node not in visited:
            visited.append(node)
            path.append((node,cnt))
            for i in range(101):
                if i in network[node]:
                    que.append((i,cnt+1))

    return path

for tc in range(1,11):
    N,start=map(int,input().split())
    lst=list(map(int,input().split()))

    network=[[]for _ in range(101)]
    v1=[]
    v2=[]
    for i in range(N):
        if i%2:
            v2.append(lst[i])
        else:
            v1.append(lst[i])

    for i in range(N//2):
        network[v1[i]].append(v2[i])

    visited=[]
    result=(BFS(start))

    maxcnt=0
    for i in result:
        if i[1]>maxcnt:
            maxcnt=i[1]

    ans=0
    for i in result:
        if i[1]==maxcnt:
            if i[0]>ans:
                ans=i[0]

    print(f'#{tc} {ans}')