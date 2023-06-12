num=int(input()) 
l1=[0 for x in range(num)]

for i in range(num): 
    a=int(input()) 
    l1[a-1]=list(map(int,input().split()))

mode=[0 for x in range(10)] 
max_count=[0 for x in range(10)] 

for i in range(num):
    for j in range(101): 
        count=0
        for k in l1[i]:
            if j==k:
                count=count+1

        if max_count[i]<=count:
            max_count[i]=count
            mode[i]=j

for x in range(10):
    print(f'#{x+1} {mode[x]}')