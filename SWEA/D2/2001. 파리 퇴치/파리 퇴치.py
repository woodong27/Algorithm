T=int(input())
for x in range(T):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split()))for _ in range(N)]
    di=[x for x in range(M)]*M
    di.sort()
    dj=[x for x in range(M)]*M

    result=[]

    for i in range(N-M+1):
        for j in range(N-M+1):
            killed=0
            for k in range(len(di)):
                ni,nj=i+di[k],j+dj[k]
                killed+=lst[ni][nj]
            result.append(killed)

    print(f'#{x+1} {max(result)}')