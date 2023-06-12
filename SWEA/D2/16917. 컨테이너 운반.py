T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    containers=list(map(int,input().split()))
    trucks=list(map(int,input().split()))

    trucks.sort()
    containers.sort()

    sum=0
    while trucks:
        truck=trucks.pop()
        while containers and containers[-1]>truck:
            containers.pop()

        if containers:
            sum+=containers.pop()
        else:
            break

    print(f'#{tc+1} {sum}')