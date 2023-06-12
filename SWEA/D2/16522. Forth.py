T=int(input())

for x in range(T):
    exp=list(map(str,input().split()))

    result=[]
    ans=0
    for i in exp:
        if i.isdigit():
            result.append(i)
        elif i=='.':
            break
        else:
            if len(result)<2:
                ans='error'
                break
            else:
                a=int(result.pop())
                b=int(result.pop())
                if i=='+':
                    result.append(b+a)
                elif i=='*':
                    result.append(b*a)
                elif i=='-':
                    result.append(b-a)
                else:
                    result.append(b//a)

    if len(result)>1:
        ans='error'

    print(f'#{x+1} {result[0] if ans==0 else ans}')