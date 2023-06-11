T=int(input())

words_lst=['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']

for x in range(T):
    tc,N=map(str,input().split())
    words=list(map(str,input().split()))
    print(f'{tc}')

    for i in words_lst:
        count=0
        for j in words:
            if i==j:
                count+=1
        print((i+' ')*count)