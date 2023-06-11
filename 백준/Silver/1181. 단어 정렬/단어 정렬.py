N=int(input())

lst=[]
for i in range(N):
    lst.append(input())

lst=list(set(lst))

lst.sort()
len_lst=[]
for i in lst:
    len_lst.append(len(i))

len_lst=list(set(len_lst))
len_lst.sort()

for i in len_lst:
    for j in lst:
        if i==len(j):
            print(j)