T=int(input())

for tc in range(T):
    N,M,K=map(int,input().split())

    arrivetime=list(map(int,input().split()))

    people=[0 for _ in range(max(arrivetime)+1)]
    for i in arrivetime:
        people[i]+=1

    ans='Possible'
    if min(arrivetime)<M:
        ans='Impossible'
    else:
        seconds=1
        bread=0
        while seconds<=max(arrivetime):
            if not seconds%M:
                bread+=K

            bread-=people[seconds]

            if bread<0:
                ans='Impossible'
                break

            seconds+=1

    print(f'#{tc+1} {ans}')