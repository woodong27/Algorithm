from collections import deque

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(si,sj,gi,gj,lst):
    que=deque([])
    que.append((si,sj))
    visited=[[0 for _ in range(100)]for _ in range(100)]
    while que:
        ci,cj=que.popleft()
        if ci==gi and cj==gj:
            return 1
        visited[ci][cj]=1
        for k in range(4):
            if 0<=ci+di[k]<100 and 0<=cj+dj[k]<100:
                ni,nj=ci+di[k],cj+dj[k]
                if not visited[ni][nj] and lst[ni][nj]!='1':
                    que.append((ni,nj))

    return 0

for x in range(10):
    tc=int(input())
    maze=[list(input())for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze[i][j]=='2':
                si,sj=i,j
            if maze[i][j]=='3':
                gi,gj=i,j

    result=bfs(si,sj,gi,gj,maze)
    print(f'#{tc} {result}')