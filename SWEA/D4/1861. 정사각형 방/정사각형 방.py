from collections import deque

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(si,sj):
    q=deque([(si,sj)])
    visited[si][sj]=1
    path=[rooms[si][sj]]
    while q:
        ci,cj=q.popleft()
        for k in range(4):
            ni,nj=ci+di[k],cj+dj[k]
            if 0<=ni<N and 0<=nj<N and abs(rooms[ni][nj]-rooms[ci][cj])==1:
                if not visited[ni][nj]:
                    q.append((ni,nj))
                    visited[ni][nj]=1
                    path.append(rooms[ni][nj])

    return min(path),len(path)

for tc in range(T):
    N=int(input())
    rooms=[list(map(int,input().split()))for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]

    ansv,ansd=N**2, 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                resultv,resultd=bfs(i,j)
                if resultd>ansd or resultd==ansd and resultv<ansv:
                    ansv=resultv
                    ansd=resultd

    print(f'#{tc+1}',ansv,ansd)