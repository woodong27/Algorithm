for x in range(10):
    N=int(input())
    equation=list(input())

    postfix=[]
    stack=[]
    for i in equation:
        if i.isdigit():
            postfix.append(int(i))
        else:
            if i=='*':
                while stack and stack[-1]=='*':
                    postfix.append(stack.pop())
                stack.append(i)
            elif i=='+':
                while stack:
                    postfix.append(stack.pop())
                stack.append(i)

    while stack:
        postfix.append(stack.pop())

    result=[]
    for i in postfix:
        if i=='+':
            result.append(result.pop()+result.pop())
        elif i=='*':
            result.append(result.pop()*result.pop())
        else:
            result.append(i)

    print(f'#{x+1} {result[0]}')