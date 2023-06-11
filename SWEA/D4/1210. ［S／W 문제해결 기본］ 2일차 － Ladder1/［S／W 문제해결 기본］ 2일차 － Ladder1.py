for x in range(10):
    T=int(input())
    ladder=[list(map(int,input().split()))for _ in range(100)]

    start=0
    depth=99
    ans=0
    for j in range(100):
        if ladder[depth][j]==2:
            start=j

    while depth!=0:
        depth-=1

        if 0<=start-1 and ladder[depth][start-1]==1:
            while True:
                start-=1
                if ladder[depth][start-1]!=1:
                    break

        elif start+1<100 and ladder[depth][start+1]==1:
            while True:
                start += 1
                if start==99 or ladder[depth][start+1]!=1:
                    break

        ans=start

    print(f'#{T} {ans}')