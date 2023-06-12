T=int(input())

def calculating(idx,point,calorie):
    global ans
    if calorie>L:
        return

    if point>ans:
        ans=point

    for i in range(idx+1,N):
        calculating(i,point+points[i],calorie+calories[i])

for tc in range(T):
    N,L=map(int,input().split())
    points,calories=[0]*N,[0]*N
    for n in range(N):
        points[n],calories[n]=map(int,input().split())

    ans=0
    calculating(-1,0,0)

    print(f'#{tc+1}',ans)