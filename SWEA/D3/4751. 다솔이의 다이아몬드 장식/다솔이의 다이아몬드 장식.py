T=int(input())

for x in range(T):
    word=input()
    ans=[[0 for _ in range(1+len(word)*4)]for _ in range(5)]

    count=0
    for i in range(len(ans[0])):
        if i%2==0 and i%4!=0:
            ans[0][i]=ans[4][i]='#'
            ans[2][i]=word[count]
            count+=1
        else:
            ans[0][i]=ans[4][i]='.'
            if i%4:
                ans[2][i]='.'
            else:
                ans[2][i]='#'

        if i%2:
            ans[1][i]=ans[3][i]='#'
        else:
            ans[1][i]=ans[3][i]='.'

    for i in range(5):
        for j in range(len(ans[i])):
            if j==len(ans[i])-1:
                print(ans[i][j])
            else:
                print(ans[i][j],end='')