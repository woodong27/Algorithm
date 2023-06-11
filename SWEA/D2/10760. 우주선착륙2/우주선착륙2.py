T=int(input())

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1]

for tc in range(T):
    N,M=map(int,input().split())
    picture=[list(map(int,input().split()))for _ in range(N)]

    ans=0
    for i in range(0,N):
        for j in range(M):
            stack=[]
            for k in range(8):
                if 0<=i+di[k]<N and 0<=j+dj[k]<M and picture[i+di[k]][j+dj[k]]<picture[i][j]:
                    stack.append(picture[i+di[k]][j+dj[k]])

            if len(stack)>=4:
                ans+=1

    print(f'#{tc+1} {ans}')