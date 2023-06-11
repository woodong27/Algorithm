for x in range(10):
    t=int(input())
    ladder=[list(map(int,input().split()))for _ in range(100)]

    ans=0
    cnt=100**2

    for i in range(100):
        depth = 0
        start = i
        if ladder[depth][i]==1:
            count=0
            while depth!=99:
                count+=1
                depth+=1
                if 0<start-1 and ladder[depth][start-1]==1:
                    while True:
                        start-=1
                        count+=1
                        if 0>start-1 or ladder[depth][start-1]!=1:
                            break

                elif start+1<100 and ladder[depth][start+1]==1:
                    while True:
                        start+=1
                        count+=1
                        if start==99 or ladder[depth][start+1]!=1:
                            break

        if cnt>count:
            cnt=count
            ans=i

    print(f'#{t} {ans}')