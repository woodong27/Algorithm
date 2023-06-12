T=int(input())

for tc in range(T):

    lst=list(input())

    ans=0
    sumv=0
    for i in range(len(lst)-1):
        temp=0
        sumv+=int(lst[i])
        if sumv<i+1:
            temp+=i+1-sumv
            sumv+=temp

        ans+=temp

    print(f'#{tc+1} {ans}')