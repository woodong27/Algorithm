import math

T = int(input())

for x in range(T):
    N = int(input())

    lst=[]
    for i in range(N):
        s, g = map(int, input().split())
        if g<s:
            s,g=g,s
        lst.append([s,g])

    corrider=[0]*201

    for i in range(N):
        start=math.ceil(lst[i][0]/2)
        end=math.ceil(lst[i][1]/2)

        for j in range(start,end+1):
            corrider[j]+=1

    print(f'#{x+1} {max(corrider)}')