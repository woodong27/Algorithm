T=int(input())

for x in range(T):
    N=int(input())
    prices=list(map(int,input().split()))

    stack=[]
    sum=0
    for i in range(len(prices)-1,-1,-1):
        if not stack:
            stack.append(prices[i])
        elif stack[-1]>prices[i]:
            sum+=stack[-1]-prices[i]
        else:
            stack.pop()
            stack.append(prices[i])

    print(f'#{x+1} {sum}')