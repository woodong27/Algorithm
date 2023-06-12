T=int(input())

def changing(i,cnt):
    global ans
    if i>=N-1:
        if ans>cnt:
            ans=cnt
        return

    if ans<cnt:
        return

    for j in range(1,batteries[i]+1):
        changing(i+j,cnt+1)

for tc in range(T):
    N,*batteries=map(int,input().split())

    ans=N-1
    changing(0,-1)

    print(f'#{tc+1} {ans}')