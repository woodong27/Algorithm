T=int(input())
for x in range(T):
    N=int(input())
    lst=list(input())
    for i in range(N):
        lst[i]=int(lst[i])
    counts=[0]*10

    for i in lst:
        counts[i]+=1

    maxv=max(counts)

    #max안쓰고 최대값 찾기
    # max_value=0
    # for i in range(len(counts)):
    #     if counts[i]>max_value:
    #         max_value=counts[i]

    ans_value, ans_count=0,0
    for i in range(9,-1,-1):
        if counts[i]==maxv:
            ans_value=i
            ans_count=counts[i]
            break

    print(f'#{x+1} {ans_value} {ans_count}')