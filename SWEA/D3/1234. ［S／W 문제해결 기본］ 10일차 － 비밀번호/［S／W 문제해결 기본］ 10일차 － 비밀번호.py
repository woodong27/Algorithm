for tc in range(10):
    N,password=map(str,input().split())

    password=list(password)

    stack=[]
    for i in password:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)

    print(f"#{tc+1} {''.join(stack)}")