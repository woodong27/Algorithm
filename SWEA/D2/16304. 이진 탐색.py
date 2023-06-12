T=int(input())

for x in range(T):
    ans=0
    P,A,B=map(int,input().split())

    start=1
    end=P
    cnt_A=0
    while True:
        middle=(start+end)//2
        cnt_A+=1
        if middle==A:
            break
        elif A>middle:
            start=middle
        else:
            end=middle

    start=1
    end=P
    cnt_B=0
    while True:
        middle=(start+end)//2
        cnt_B+=1
        if middle==B:
            break
        elif B>middle:
            start=middle
        else:
            end=middle

    if cnt_A<cnt_B:
        ans='A'
    elif cnt_A>cnt_B:
        ans='B'

    print(f'#{x+1} {ans}')