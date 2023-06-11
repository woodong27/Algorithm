T=int(input())

for x in range(T):
    N,M=map(int,input().split())

    picture=[list(map(int,input().split()))for _ in range(N)]
    picture_t=list(map(list,zip(*picture)))

    ans=0

    for i in picture:
        stack=[]
        for j in i:
            if j==1:
                stack.append(j)
            else:
                if ans<=len(stack):
                    ans=len(stack)
                    while stack:
                        stack.pop()

            if len(stack)>=ans:
                ans=len(stack)

    for k in picture_t:
        stack=[]
        for l in k:
            if l==1:
                stack.append(l)
            else:
                if ans<=len(stack):
                    ans=len(stack)
                    while stack:
                        stack.pop()

            if len(stack)>=ans:
                ans=len(stack)

    print(f'#{x+1} {ans}')