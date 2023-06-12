T=int(input())

def backtrack(sumv,i):
    global minv
    if i==N:
        if sumv<=minv:
            minv=sumv
            return
    elif sumv>minv:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j]=1
                backtrack(sumv+lst[i][j],i+1)
                visited[j]=0

for x in range(T):
    N=int(input())
    lst=[list(map(int,input().split()))for _ in range(N)]

    visited=[0]*N
    sumv=0
    minv=N*10

    backtrack(sumv,0)

    print(f'#{x+1} {minv}')