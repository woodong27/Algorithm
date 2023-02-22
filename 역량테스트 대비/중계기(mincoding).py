import math

T=int(input())

for tc in range(T):
    N=int(input())
    N+=1

    village=[list(map(int,input().split()))for _ in range(N)]

    houses=[]
    ri,rj=0,0
    for i in range(N):
        for j in range(N):
            if village[i][j]==2:
                ri,rj=i,j
            if village[i][j]==1:
                houses.append((i,j))

    d=0
    for house in houses:
        distance=(house[0]-ri)**2+(house[1]-rj)**2
        if distance>d:
            d=distance
            fi,fj=house[0],house[1]

    ans=math.ceil(d**(1/2))
    print(f'#{tc+1} {ans}')