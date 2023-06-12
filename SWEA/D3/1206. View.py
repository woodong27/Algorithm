for x in range(10):
    N=int(input())
    lst=list(map(int,input().split()))
    sum=0
    for i in range(2,N-2):
        temp=lst[i-2:i+3]
        if temp[2]==max(temp):
            temp=sorted(temp)
            sum=sum+temp[-1]-temp[-2]

    print(f'#{x+1} {sum}')