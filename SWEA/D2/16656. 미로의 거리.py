from collections import deque

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def BFS(i,j,ei,ej):
    que=deque([])
    que.append((i,j,-1))
    ans=0
    while que:
        ci,cj,cnt=que.popleft()
        visited[ci][cj]=1
        if ci==ei and cj==ej:
            return cnt
        for k in range(4):
            if 0<=ci+di[k]<N and 0<=cj+dj[k]<N:
                ni=ci+di[k]
                nj=cj+dj[k]
                if maze[ni][nj]!='1' and not visited[ni][nj]:
                    que.append((ni,nj,cnt+1))

    return ans

for tc in range(T):
    N=int(input())
    maze=[list(input())for _ in range(N)]
    visited=[[0 for _ in range(N)]for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                si,sj=i,j
            if maze[i][j]=='3':
                gi,gj=i,j

    result=BFS(si,sj,gi,gj)
    print(f'#{tc+1} {result}')