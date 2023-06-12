T=int(input())

for x in range(T):
    K,N,M=map(int,input().split())
    charger=list(map(int,input().split()))

    pos=0
    count=0
    station=0
    temp=pos+K

    while temp<N:
        for i in charger:
            if pos<i and i<=temp:
                station=i
            elif temp<i:
                break

        if station==-1:
            count=0
            break

        pos=station
        temp=pos+K
        count+=1
        station=-1

    print(f'#{x+1} {count}')