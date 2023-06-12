T=int(input())

def binarytree(n):
    global num
    if n<N+1:
        binarytree(n*2)
        tree[n]=num
        num+=1
        binarytree(n*2+1)

for tc in range(T):
    N=int(input())

    n,num,tree=1,1,[0]*(N+1)
    binarytree(n)

    print(f'#{tc+1} {tree[1]} {tree[N//2]}')