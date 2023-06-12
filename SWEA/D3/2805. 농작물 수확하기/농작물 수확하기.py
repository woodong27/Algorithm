T=int(input())

for tc in range(T):
    N=int(input())
    farm=[list(map(int,input()))for _ in range(N)]

    ci=cj=N//2
    profit=0
    for i in range(N):
        for j in range(N):
            if abs(ci-i)+abs(cj-j)<=N//2:
                profit+=farm[i][j]

    print(f'#{tc+1} {profit}')