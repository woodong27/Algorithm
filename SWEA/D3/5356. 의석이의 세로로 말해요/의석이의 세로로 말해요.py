T=int(input())

for tc in range(T):
    words=[list(input())for _ in range(5)]

    maxlen=0
    for i in words:
        if len(i)>maxlen:
            maxlen=len(i)

    for i in words:
        while len(i)!=maxlen:
            i.append('blank')

    words_t=list(map(list,zip(*words)))
    ans=[]
    for i in words_t:
        for j in i:
            if j!='blank':
                ans.append(j)

    print(f'#{tc+1} ',*ans,sep='')