T=int(input())

def binary_search(l,r):
    global cnt, flag
    m=(l+r)//2

    if A[m]==num:
        cnt+=1
        return
    elif num<A[m]:
        if flag=='L':
            return
        flag='L'
        binary_search(l,m-1)
    elif num>A[m]:
        if flag=='R':
            return
        flag='R'
        binary_search(m+1,r)

for tc in range(T):
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    B=list(map(int,input().split()))

    cnt=0
    for num in B:
        flag=0
        binary_search(0,N-1)

    print(f'#{tc+1} {cnt}')