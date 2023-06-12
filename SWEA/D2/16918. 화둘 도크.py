T=int(input())

for tc in range(T):
    N=int(input())

    times=[0]*N
    for n in range(N):
        times[n]=list(map(int,input().split()))

    times.sort(key=lambda x:(x[1],x[0]))
    cnt=0
    while times:
        s,e=times.pop(0)
        while times and times[0][0]<e:
            times.pop(0)
        cnt+=1

    print(f'#{tc+1} {cnt}')