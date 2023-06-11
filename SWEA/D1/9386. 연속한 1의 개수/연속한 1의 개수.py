T=int(input())

for x in range(T):
    N=int(input())
    string=input()
    lst=string.split('0')
    new_lst=[]
    for i in lst:
        if i!='':
            new_lst.append(i)

    max=0
    for i in new_lst:
        if len(i)>=max:
            max=len(i)

    print(f'#{x+1} {max}')