T=int(input())
for x in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    lst.sort()
    print(f'#{x+1}',*lst)