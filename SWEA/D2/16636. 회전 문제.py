T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    numbers=list(map(int,input().split()))

    for i in range(M):
        numbers.append(numbers.pop(0))

    print(f'#{tc+1} {numbers[0]}')