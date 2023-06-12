T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    lst=list(map(int,input().split()))
    
    temp=[] 
    for idx,cheese in enumerate(lst):
        temp.append((idx+1,cheese))

    pizza=[]
    for i in range(N):
        pizza.append(temp.pop(0))

    while pizza:
        idx,cheese=pizza.pop(0)
        cheese//=2
        if cheese!=0:
            pizza.append((idx,cheese))
        elif temp:
            pizza.append(temp.pop(0))
        else:
            ans=idx

    print(f'#{tc+1} {ans}')