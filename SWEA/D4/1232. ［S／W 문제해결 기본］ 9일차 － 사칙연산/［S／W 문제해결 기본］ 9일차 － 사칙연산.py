def calculate(n):
    if op[n]:
        a=calculate(op[n][0])
        b=calculate(op[n][1])
        if tree[n]=='+':
            return a+b
        elif tree[n]=='-':
            return a-b
        elif tree[n]=='*':
            return a*b
        else:
            return a/b
    return tree[n]

for tc in range(1,11):
    N=int(input())

    tree=[0 for _ in range(N+1)]
    op=[[]for _ in range(N+1)]
    for i in range(N):
        lst=list(map(str,input().split()))
        if lst[1].isdigit():
            tree[int(lst[0])]=int(lst[1])
        else:
            tree[int(lst[0])]=lst[1]
            op[int(lst[0])].append(int(lst[2]))
            op[int(lst[0])].append(int(lst[3]))

    result=int(calculate(1))
    print(f'#{tc} {result}')