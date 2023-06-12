T=int(input())

def counting(n):
    global cnt
    if tree[n]!=[]:
        cnt += len(tree[n])
        if len(tree[n])>1:
            counting(tree[n][0])
            counting(tree[n][1])
        else:
            counting(tree[n][0])

for tc in range(T):
    E,N=map(int,input().split())
    V=E+1

    temp=list(map(int,input().split()))

    tree=[[]for _ in range(V+1)]
    for i in range(0,E*2,2):
        tree[temp[i]].append(temp[i+1])

    cnt=1
    counting(N)

    print(f'#{tc+1} {cnt}')