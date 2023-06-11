T=int(input())

for x in range(T):
    lst=[list(input())for _ in range(5)]

    N=0
    for i in range(5):
        if N<=len(lst[i]):
            N=len(lst[i])

    temp=[[0 for _ in range(N)]for _ in range(N)]

    for i in range(5):
        for j in range(len(lst[i])):
            temp[i][j]=lst[i][j]

    for i in range(N):
        for j in range(N):
            if i<j:
                temp[i][j],temp[j][i]=temp[j][i],temp[i][j]

    if x>0:
        print()
    print(f'#{x+1}',end=' ')
    for i in range(N):
        for j in range(N):
            if temp[i][j]!=0:
                print(temp[i][j],end='')