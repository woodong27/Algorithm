T=int(input())

di = [-1,1,0,0]
dj = [0,0,-1,1]

for x in range(T):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split()))for x in range(N)]

    result=[]

    for i in range(N):
        for j in range(M):
            sum=lst[i][j]
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    sum+=lst[ni][nj]
                result.append(sum)

    print(f'#{x+1} {max(result)}')