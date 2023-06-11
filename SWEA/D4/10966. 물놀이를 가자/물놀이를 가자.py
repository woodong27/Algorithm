from collections import deque

di=(-1,1,0,0)
dj=(0,0,-1,1)

T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    pool=[list(input())for _ in range(N)]
    visited = [[1e4 for _ in range(M)] for _ in range(N)]
    q = deque([])
    for i in range(N):
        for j in range(M):
            if pool[i][j]=='W':
                visited[i][j]=0
                q.append((i,j))

    while q:
        ci, cj = q.popleft()
        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj]>visited[ci][cj]+1:
                q.append((ni, nj))
                visited[ni][nj]=visited[ci][cj]+1

    ans=0
    for row in visited:
        ans+=sum(row)

    print(f'#{tc+1} {ans}')