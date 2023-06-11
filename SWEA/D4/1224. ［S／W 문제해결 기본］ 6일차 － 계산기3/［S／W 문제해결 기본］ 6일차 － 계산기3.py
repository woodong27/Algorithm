for tc in range(10):
    N=int(input())
    equation=input()

    postfix=[]
    stack=[]
    for i in equation:
        if i=='(':
            stack.append(i)
        elif i.isdigit():
            postfix.append(int(i))
        elif i==')':
            while stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()
        elif i=='+':
            while stack[-1]=='*':
                postfix.append(stack.pop())
            stack.append(i)
        else:
            stack.append(i)

    result=[]
    for i in postfix:
        if i=='+':
            result.append(result.pop()+result.pop())
        elif i=='*':
            result.append(result.pop()*result.pop())
        else:
            result.append(i)

    print(f'#{tc+1} {result[0]}')