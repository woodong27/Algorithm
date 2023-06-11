for _ in range(10):
    T=int(input())
    lst=[list(input())for x in range(100)]

    for i in range(100):
        lst[i]=''.join(lst[i])

    lst_t=list(map(list,zip(*lst)))
    for i in range(100):
        lst_t[i]=''.join(lst_t[i])

    ans=0
    for i in range(100):
        start=0
        j=0
        while start+j<100:
            j+=1
            if lst[i][start:start+j+1]==lst[i][start:start+j+1][::-1]:
                if len(lst[i][start:start+j+1])>=ans:
                    ans=len(lst[i][start:start+j+1])

            if lst_t[i][start:start+j+1]==lst_t[i][start:start+j+1][::-1]:
                if len(lst_t[i][start:start+j+1])>=ans:
                    ans=len(lst_t[i][start:start+j+1])

            if start+j==100:
                start+=1
                j=0

    print(f'#{T} {ans}')