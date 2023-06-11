T=int(input())

for x in range(T):
    N,K=map(int,input().split())
    puzzle=[list(map(int,input().split()))for _ in range(N)]

    row=[]
    col=[]
    for i in range(N):
        row_w=[]
        col_w=[]
        for j in range(N):
            row_w.append(str(puzzle[i][j]))
            col_w.append(str(puzzle[j][i]))
        row.append(''.join(row_w))
        col.append(''.join(col_w))

    for i in range(N):
        row[i]=row[i].split('0')
        col[i]=col[i].split('0')

    count=0
    for i in range(N):
        for j in row[i]:
            if len(j)==K:
                count+=1

        for j in col[i]:
            if len(j)==K:
                count+=1

    print(f'#{x+1} {count}')