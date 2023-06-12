T=int(input())

for x in range(T):
    D,A,B,F=map(int,input().split())

    print(f'#{x+1} {D/(A+B)*F}')