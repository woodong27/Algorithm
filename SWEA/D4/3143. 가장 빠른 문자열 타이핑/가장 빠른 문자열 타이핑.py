T=int(input())

for x in range(T):

    A,B=map(str,input().split())

    count = 0
    while B in A:
        A=A.replace(B,'',1)
        count += 1

    print(f'#{x+1} {count+len(A)}')