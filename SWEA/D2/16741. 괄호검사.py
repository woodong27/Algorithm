T=int(input())

for x in range(T):
    word=list(input())

    stack=[]
    for i in word:
        if i=='{' or i=='(':
            stack.append(i)

        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
                

        elif i=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(i)

    ans=1
    if len(stack)>0:
        ans=0

    print(f'#{x+1} {ans}')