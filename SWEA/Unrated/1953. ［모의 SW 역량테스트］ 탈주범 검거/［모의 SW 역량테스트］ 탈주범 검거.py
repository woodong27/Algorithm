T=int(input())

from collections import deque

#1:상하좌우 2:상하 3:좌우 4:상우 5:하우 6:하좌 7:상좌
directions={1:((-1,0),(1,0),(0,-1),(0,1)), 2:((-1,0),(1,0)), 3:((0,-1),(0,1)),
           4:((-1,0),(0,1)), 5:((1,0),(0,1)), 6:((1,0),(0,-1)), 7:((-1,0),(0,-1))}

for tc in range(T):
    N,M,si,sj,L=map(int,input().split())
    tunnel=[list(map(int,input().split()))for _ in range(N)]
    visited=[[0 for _ in range(M)]for _ in range(N)]

    q=deque([(si,sj,0)])
    visited[si][sj]=1
    path=[(si,sj)]
    while q:
        ci,cj,cnt=q.popleft()
        dir=directions[tunnel[ci][cj]]
        for di,dj in dir:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<M and tunnel[ni][nj]!=0 and not visited[ni][nj]:
                for ii,jj in directions[tunnel[ni][nj]]:
                    if ii+di==0 and jj+dj==0 and cnt+1<L:
                        q.append((ni,nj,cnt+1))
                        visited[ni][nj]=1
                        path.append((ni,nj))

    ans=len(path)
    print(f'#{tc+1} {ans}')