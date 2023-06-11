T=int(input())

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1] #상,하,좌,우,11시,1시,5시,7시

for tc in range(T):
    N,M=map(int,input().split())

    board=[[0 for _ in range(N)]for _ in range(N)]
    board[N//2-1][N//2-1]=2
    board[N//2-1][N//2]=1
    board[N//2][N//2-1]=1
    board[N//2][N//2]=2

    for x in range(M):
        temp_i,temp_j,color=map(int,input().split())
        i,j=temp_i-1,temp_j-1
        board[i][j]=color

        for k in range(8):
            if 0<=i+di[k]<N and 0<=j+dj[k]<N:
                ni,nj=i+di[k],j+dj[k]
                while 0<=ni+di[k]<N and 0<=nj+dj[k]<N and board[ni][nj] not in [color, 0]:
                    if board[ni+di[k]][nj+dj[k]]==color:
                        tempi,tempj=ni,nj
                        while board[tempi][tempj]!=color:
                            board[tempi][tempj]=color
                            tempi -= di[k]
                            tempj -= dj[k]
                    ni+=di[k]
                    nj+=dj[k]

    cnt_1,cnt_2=0,0
    for c in range(N):
        for r in range(N):
            if board[c][r]==1:
                cnt_1+=1
            elif board[c][r]==2:
                cnt_2+=1

    print(f'#{tc+1} {cnt_1} {cnt_2}')