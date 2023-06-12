T=int(input())

def game(lst):
    n=len(lst)
    if n==1:
        return lst[0]

    elif n==2:
        if lst[0][1]-lst[1][1]==2:
            return lst[1]
        elif lst[0][1]-lst[1][1]==-2:
            return lst[0]
        elif lst[0][1]==lst[1][1]:
            return lst[0]
        elif lst[0][1]-lst[1][1]==1:
            return lst[0]
        elif lst[0][1]-lst[1][1]==-1:
            return lst[1]

    else:
        if n%2:
            l1=game(lst[0:n//2+1])
            l2=game(lst[n//2+1:n])
            return game([l1,l2])

        else:
            l1=game(lst[0:n//2])
            l2=game(lst[n//2:n])
            return game([l1,l2])

for x in range(T):
    N=int(input())
    cards=list(map(int,input().split()))

    new=[]
    for i in enumerate(cards):
        new.append(i)

    print(f'#{x+1} {game(new)[0]+1}')