T=int(input())

for x in range(T):
    str1=list(set(input()))
    str2=list(input())

    max_v=0
    for i in str1:
        count=0
        for j in str2:
            if i==j:
                count+=1
        if count>=max_v:
            max_v=count

    print(f'#{x+1} {max_v}')