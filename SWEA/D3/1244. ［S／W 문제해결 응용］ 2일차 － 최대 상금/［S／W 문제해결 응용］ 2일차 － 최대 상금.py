T=int(input())

def trading(cnt):
    global ans
    num=''.join(numbers)
    if cnt==trade:
        if ans<num:
            ans=num
        return

    if num in visited:
        return

    else:
        visited.append(num)
        for i in range(n):
            for j in range(i+1,n):
                numbers[i],numbers[j]=numbers[j],numbers[i]
                trading(cnt+1)
                numbers[i],numbers[j]=numbers[j],numbers[i]

for tc in range(T):
    num,trade=map(int,input().split())

    numbers=list(str(num))
    n=len(numbers)
    visited=[]

    ans='000000'
    trading(0)

    print(f'#{tc+1} {ans}')