T=int(input())

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,-1,1]

def omok():
    for i in range(N):
        for j in range(N):
            if board[i][j]=='o':
                for k in range(8):
                    cnt=0
                    for m in range(1,5):
                        ni,nj=i+di[k]*m,j+dj[k]*m
                        if 0<=ni<N and 0<=nj<N and board[ni][nj]=='o':
                            cnt+=1

                    if cnt>=4:
                        return 'YES'

    return 'NO'

for tc in range(T):
    N=int(input())
    board=[list(input())for _ in range(N)]

    ans=omok()
    print(f'#{tc+1} {ans}')