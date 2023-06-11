T=int(input())

for x in range(T):
    print(f'#{x + 1}')

    N=int(input())
    tri=[[]for _ in range(N)]
    tri[0].append(1)

    for i in range(1,N):
        tri[i].append(1)
        stack=tri[i-1][:]
        for j in range(1,i):
            tri[i].append(stack.pop()+stack[-1])
        tri[i].append(1)

    for i in range(N):
        print(*tri[i])