T=int(input())

for tc in range(T):
    N,M=map(int,input().split())

    flag=[list(input())for _ in range(N)]

    minv=N*M
    for w in range(N-2):
        for b in range(w+1,N-1):
            cnt=0
            for j in range(M):
                for iw in range(w+1):
                    if flag[iw][j]!='W':
                        cnt+=1

                for ib in range(w+1,b+1):
                    if flag[ib][j]!='B':
                        cnt+=1

                for ir in range(b+1,N):
                    if flag[ir][j]!='R':
                        cnt+=1

            if minv>cnt:
                minv=cnt

    print(f'#{tc+1} {minv}')