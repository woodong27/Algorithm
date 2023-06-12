T=int(input())

def calculating(idx,sumv):
    global ans
    if sumv==K:
        ans+=1
        return

    if sumv>K:
        return

    for j in range(idx+1,N):
        if not used[j]:
            used[j]=1
            calculating(j,sumv+numbers[j])
            used[j]=0

for tc in range(T):
    N,K=map(int,input().split())
    numbers=list(map(int,input().split()))

    ans=0
    used=[0]*N
    for i in range(N):
        calculating(i,numbers[i])

    print(f'#{tc+1}', ans)