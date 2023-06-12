T=int(input())

def backtrack(i,sumv):
    global ans
    if i==N:
        if sumv<ans:
            ans=sumv
        return

    elif sumv>ans:
        return

    for j in range(N):
        if not visited[j]:
            visited[j]=1
            backtrack(i+1,sumv+prices[i][j])
            visited[j]=0

for tc in range(T):
    N=int(input())
    prices=[list(map(int,input().split()))for _ in range(N)]

    visited=[0]*N
    ans=99*N
    backtrack(0,0)

    print(f'#{tc+1} {ans}')