T=int(input())

for tc in range(T):
    N=int(input())

    number=[]
    k=1
    while len(number)!=10:
        num=N*k
        temp=list(str(num))

        for i in temp:
            if i not in number:
                number.append(i)

        k+=1

    ans=N*(k-1)
    print(f'#{tc+1} {ans}')