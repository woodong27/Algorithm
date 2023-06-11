T=int(input())

for x in range(T):
    print(f'#{x+1}')
    N=int(input())
    lst=[list(map(str,input().split()))for _ in range(N)]

    word=[]
    for i in range(N):
        word.append(list(lst[i][0]*int(lst[i][1])))

    ans=[]
    for i in range(len(word)):
        for j in range(len(word[i])):
            ans.append(word[i][j])

    for i in range(len(ans)):
        if i==len(ans)-1:
            print(ans[i])
        else:
            if i!=0 and i%10==0:
                print()
            print(ans[i],end='')