T=int(input())

def rotate_90_degree(list,n):
    rotated_l=[[0 for x in range(n)]for x in range(n)]
    for a in range(n):
        for b in range(n):
            rotated_l[b][n-1-a]=list[a][b]

    return rotated_l

for x in range(T):
    N=int(input())
    l=[list(map(int,input().split()))for _ in range(N)]
    ans=[[]for _ in range(N)]

    l_90=rotate_90_degree(l,N)
    l_180=rotate_90_degree(l_90,N)
    l_270=rotate_90_degree(l_180,N)

    for i in range(N):
        for j in range(N):
            ans[i].append(l_90[i][j])
        ans[i].append(' ')

        for j in range(N):
            ans[i].append(l_180[i][j])
        ans[i].append(' ')

        for j in range(N):
            ans[i].append(l_270[i][j])

    print(f'#{x+1}')
    for i in range(N):
        for j in range(len(ans[i])):
            if j==len(ans[i])-1:
                print(ans[i][j])
            else:
                print(ans[i][j],end='')
