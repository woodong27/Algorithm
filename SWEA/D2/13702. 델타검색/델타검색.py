for x in range(10):
    N=int(input())
    lst=[list(map(int,input().split()))for _ in range(N)]

    di=[-1,1,0,0]
    dj=[0,0,-1,1]

    sum=0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<N:
                    sum=sum+abs(lst[ni][nj]-lst[i][j])

    print(f'#{x+1} {sum}')
