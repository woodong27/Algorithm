for x in range(10):
    N=int(input())
    lst=[list(map(int,input().split()))for _ in range(N)]

    di=[-1,1,0,0] #방향배열 사용해서 상하좌우를 탐색
    dj=[0,0,-1,1]

    sum=0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<N: #델타이동(상하좌우)이동 한 결과가 인덱스 범위 안 일때만 연산
                    sum=sum+abs(lst[ni][nj]-lst[i][j])

    print(f'#{x+1} {sum}')

    #풍선팡2도 델타연습에 좋을듯