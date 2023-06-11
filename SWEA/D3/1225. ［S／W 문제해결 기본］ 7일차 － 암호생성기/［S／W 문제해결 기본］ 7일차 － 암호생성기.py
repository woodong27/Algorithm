for _ in range(10):
    tc=int(input())
    que=list(map(int,input().split()))

    cnt=1
    while que[-1]>0:
        que.append(que.pop(0)-cnt)
        cnt+=1
        if cnt==6:
            cnt=1

    que[-1]=0

    print(f'#{tc}',*que)