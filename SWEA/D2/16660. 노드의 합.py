T=int(input())

for tc in range(T):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)

    for i in range(M):
        node,num=map(int,input().split())
        tree[node]=num

    for i in range(N,0,-1):
        if i//2>0:
            tree[i//2]+=tree[i]

    print(f'#{tc+1} {tree[L]}')