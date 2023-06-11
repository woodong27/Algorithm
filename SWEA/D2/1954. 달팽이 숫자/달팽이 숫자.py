T=int(input())

di=[0,1,0,-1]
dj=[1,0,-1,0] # 우 하 좌 상 순서의 방향 배열

for x in range(T):
    N=int(input())

    snail=[[1 for _ in range(N+2)]for _ in range(N+2)]

    for k in range(1,N+1):
        for l in range(1,N+1):
            snail[k][l]=0

    d=0
    count=1
    i=1 # 행
    j=1 # 열
    while True:
        if snail[i][j]==0:
            snail[i][j]=count
            if 1<=i+di[d]<=N and 1<=j+dj[d]<=N:
                i+=di[d]
                j+=dj[d]
                if snail[i][j]!=0:
                    i-=di[d]
                    j-=dj[d]
        if snail[i][j]!=0:
            d+=1
            if d>=4:
                d=0
            i+=di[d]
            j+=dj[d]

        count+=1
        if count>N**2:
            break

    result=[]
    for i in range(1,N+1):
        result.append(snail[i][1:N+1])

    print(f'#{x+1}')
    for i in range(N):
        print(*result[i])