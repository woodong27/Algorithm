T=int(input())

for x in range(T):
    N=int(input())
    A,B,C=[],[],[]
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
    P=int(input())
    cc=0
    for i in range(P):
        c=int(input())
        C.append(c)

    count = [0 for _ in range(5001)]
    for i in range(N):
        for j in range(A[i],B[i]+1):
            count[j]+=1

    print(f'#{x+1}',end=' ')
    for i in C:
        if i==C[-1]:
            print(count[i])
        else:
            print(count[i],end=' ')