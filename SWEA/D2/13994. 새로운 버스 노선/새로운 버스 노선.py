T=int(input())

for x in range(T):
    N=int(input())
    count=[]

    for y in range(N):
        bus,A,B=map(int,input().split())
        lst = [0] * (B + 1)
        lst[A], lst[B] = 1, 1
        if bus==1:
            for i in range(A+1,B):
                lst[i]+=1

        elif bus==2:
            if A%2==0:
                for i in range(A+1,B):
                    if i%2==0:
                        lst[i]+=1
            else:
                for i in range(A+1,B):
                    if i%2!=0:
                        lst[i]+=1

        elif bus==3:
            if A%2==0:
                for i in range(A+1,B):
                    if i%4==0:
                        lst[i]+=1
            else:
                for i in range(A+1,B):
                    if i%3==0 and i%10!=0:
                        lst[i]+=1

        if len(count)<len(lst):
            while len(count)!=len(lst):
                count.append(0)

        for i in range(len(lst)):
            if lst[i]==1:
                count[i]+=1

    print(f'#{x+1} {max(count)}')