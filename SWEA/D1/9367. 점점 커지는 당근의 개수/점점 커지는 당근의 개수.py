T=int(input())

for x in range(T):
    N=int(input())
    carrots=list(map(int,input().split()))

    count=1
    max=1
    for i in range(N-1):
        if carrots[i]+1==carrots[i+1]:
            count+=1
            if max<=count:
                max=count
        else:
            count=1

    print(f'#{x+1} {max}')