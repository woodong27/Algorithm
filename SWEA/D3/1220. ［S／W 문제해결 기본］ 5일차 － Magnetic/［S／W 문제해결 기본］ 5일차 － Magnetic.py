for tc in range(1,11):
    N=int(input())
    table=[list(map(int,input().split()))for _ in range(N)]

    result=0
    for i in range(N):
        for j in range(N):
            if table[i][j]==1:
                table[i][j]=0
                for ii in range(i+1,N):
                    if table[ii][j]==1:
                        table[ii][j]=0
                    elif table[ii][j]==2:
                        result+=1
                        break

            elif table[i][j]==2:
                table[i][j]=0
                for ii in range(i-1,-1,-1):
                    if table[ii][j]==2:
                        table[ii][j]=0
                    elif table[ii][j]==1:
                        result+=1
                        break

    print(f'#{tc} {result}')