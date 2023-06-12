T=int(input())

for x in range(T):
    ans=0
    N,M=map(int,input().split())
    lst=[0 for x in range(N)]
    for i in range(N):
        lst[i]=list(input())

    row=[]
    col=[]
    for i in range(N):
        row_w=[]
        col_w=[]
        for j in range(N):
            row_w.append(lst[i][j])
            col_w.append(lst[j][i])
        row.append(row_w)
        col.append(col_w)

    for i in range(N):
        for j in range(N-M+1):
            if row[i][j:j+M]==row[i][j:j+M][::-1]:
                ans=''.join(row[i][j:j+M])
            elif col[i][j:j+M]==col[i][j:j+M][::-1]:
                ans = ''.join(col[i][j:j + M])

    print(f'#{x+1} {ans}')