for x in range(10):
    N=int(input())
    lst=list(input())

    plus=[]
    number=[]

    for i in lst:
        if i=='+':
            plus.append(i)
        else:
            number.append(i)

    number.extend(plus)

    result=[]
    for i in number:
        if i=='+':
            a=result.pop()
            b=result.pop()
            result.append(int(b)+int(a))
        else:
            result.append(i)

    print(f'#{x+1} {result[0]}')