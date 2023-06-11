T=int(input())

def keeper(ci,cj,k):
    cost=k*k+(k-1)*(k-1)
    cnt=0
    for i in range(-(k-1),k):
        for j in range(-(k-1),k):
            if 0<=ci+i<N and 0<=cj+j<N and abs(i)+abs(j)<k:
                if village[ci+i][cj+j]==1:
                    cnt+=1

    profit=M*cnt
    if profit>=cost:
        return cnt

    return 0

for tc in range(T):
    N,M=map(int,input().split())
    village=[list(map(int,input().split()))for _ in range(N)]

    ans=0
    for i in range(N):
        for j in range(N):
            for size in range(1,N*2):
                result=keeper(i,j,size)
                if result>ans:
                    ans=result

    print(f'#{tc+1} {ans}')