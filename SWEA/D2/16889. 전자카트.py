T=int(input())

def backtrack(cnt,i,total):
    global ans
    if cnt==N:
        total+=consumption[i][0]
        if total<ans:
            ans=total
            return

    elif total>ans:
        return

    for j in range(1,N):
        if not consumption[i][j] and not visited[j]:
            continue
        elif not visited[j]:
            visited[j]=1
            backtrack(cnt+1,j,total+consumption[i][j])
            visited[j]=0

for tc in range(T):
    N=int(input())
    consumption=[list(map(int,input().split()))for _ in range(N)]

    visited=[0]*N

    ans=100*N
    backtrack(1,0,0)

    print(f'#{tc+1} {ans}')