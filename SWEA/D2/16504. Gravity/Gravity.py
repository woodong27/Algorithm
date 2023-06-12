T = int(input())

for x in range(T):
    N=int(input())
    lst=list(map(int, input().split()))
    max=0
    for i in range(N):
        cnt=0
        for j in range(i+1,N):
            if lst[i]>lst[j]:
                cnt+=1

        if max<=cnt:
            max=cnt

    print(f'#{x+1} {max}')