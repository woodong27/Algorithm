T=int(input())

for tc in range(T):
    N,Q=map(int,input().split())

    boxes=[0 for _ in range(N+1)]

    for i in range(Q):
        L,R=map(int,input().split())

        for j in range(L,R+1):
            boxes[j]=i+1

    ans=boxes[1:N+1]

    print(f'#{tc+1}',*ans)