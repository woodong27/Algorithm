T=int(input())
#내장함수 사용 금지(sort, min, max...etc)
for x in range(T):
    N=int(input())
    lst=list(map(int,input().split()))

    for i in range(N-1):
        if i%2:
            for j in range(i+1,N):
                if lst[i]>lst[j]:
                    lst[i],lst[j]=lst[j],lst[i]
        else:
            for j in range(i+1,N):
                if lst[i]<lst[j]:
                    lst[i],lst[j]=lst[j],lst[i]

    if len(lst)>10:
        lst=lst[:10]

    print(f'#{x+1}',*lst)