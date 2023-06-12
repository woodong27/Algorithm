T=int(input())

directions=((0,1),(1,0))

def moving(i,j,sumv):
    global ans
    if i==N-1 and j==N-1:
        if sumv<ans:
            ans=sumv
            return

    elif sumv>ans:
        return

    for di,dj in directions:
        ni,nj=i+di,j+dj
        if 0<=ni<N and 0<=nj<N:
            moving(ni,nj,sumv+board[ni][nj])

for tc in range(T):
    N=int(input())
    board=[list(map(int,input().split()))for _ in range(N)]

    ans=10*N
    moving(0,0,board[0][0])

    print(f'#{tc+1} {ans}')