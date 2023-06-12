T=int(input())

for tc in range(T):
    num=float(input())

    cnt=0
    ans=[]
    flag=0
    while num!=1:
        cnt+=1
        num*=2
        if num>1:
            ans.append(1)
            num-=1
        elif num<1:
            ans.append(0)

        if cnt>13:
            flag=1
            break

    print(f'#{tc+1}',end=' ')
    if flag:
        print('overflow')
    else:
        ans.append(1)
        print(*ans,sep='')