T=int(input())

dir1=((-1,0),(1,0),(0,-1),(0,1))
dir2=((-1,-1),(-1,1),(1,-1),(1,1))

for tc in range(T):
    N,M=map(int,input().split())

    flies=[list(map(int,input().split()))for _ in range(N)]
    ans=0
    for i in range(N):
        for j in range(N):
            temp1=flies[i][j]
            for di,dj in dir1:
                for m in range(1,M):
                    ni,nj=i+di*m,j+dj*m
                    if 0<=ni<N and 0<=nj<N:
                        temp1+=flies[ni][nj]

            temp2=flies[i][j]
            for di,dj in dir2:
                for m in range(1,M):
                    ni,nj=i+di*m,j+dj*m
                    if 0<=ni<N and 0<=nj<N:
                        temp2+=flies[ni][nj]

            if temp1>temp2:
                if ans<temp1:
                    ans=temp1
            elif temp1<=temp2:
                if ans<temp2:
                    ans=temp2

    print(f'#{tc+1} {ans}')