from collections import deque

T=int(input())

directions=((-1,0),(1,0),(0,-1),(0,1))

def bfs():
    global ans
    q=deque([(0,0,0)])
    while q:
        ci,cj,consumption=q.popleft()
        if ci==N-1 and cj==N-1:
            if consumption<ans:
                ans=consumption
            continue
        for di,dj in directions:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                visited[ni][nj]=1
                if mountain[ni][nj]>mountain[ci][cj]:
                    q.append((ni,nj,(mountain[nj][nj]-mountain[ci][cj])*2))
                elif mountain[ni][nj]==mountain[ci][cj]:
                    q.append((ni,nj,consumption+1))
                else:
                    q.append((ni,nj,consumption))

for tc in range(T):
    N=int(input())
    mountain=[list(map(int,input().split()))for _ in range(N)]
    visited=[[0]*N for _ in range(N)]

    ans=9*N*N
    bfs()

    print(f'#{tc+1}', ans)