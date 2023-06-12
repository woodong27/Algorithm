T=int(input())

directions=((0,-1),(0,1),(-1,0),(1,0))

def connecting(si,sj,num):
    global results
    if len(num)==7:
        results.add(num)
        return

    for di,dj in directions:
        ni,nj=si+di,sj+dj
        if 0<=ni<4 and 0<=nj<4:
            connecting(ni,nj,num+str(boards[ni][nj]))

for tc in range(T):
    boards=[list(map(int,input().split()))for _ in range(4)]

    results=set()
    for i in range(4):
        for j in range(4):
            connecting(i,j,str(boards[i][j]))

    print(f'#{tc+1}',len(results))