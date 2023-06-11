def exp(n,m):
    if m==1:
        return n
    else:
        return n*exp(n,m-1)

for _ in range(10):
    tc=int(input())
    N,M=map(int,input().split())

    print(f'#{tc} {exp(N,M)}')