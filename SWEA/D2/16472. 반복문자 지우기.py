T=int(input())

for x in range(T):
    stack=[]
    lst=list(input())
    for i in lst:
        if stack!=[]:
            if stack[-1]!=i:
                stack.append(i)
            else:
                stack.pop()
        else:
            stack.append(i)

    print(f'#{x+1} {len(stack)}')