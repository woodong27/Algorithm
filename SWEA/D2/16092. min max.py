T=int(input())
for i in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    print(f'#{i+1} {max(lst)-min(lst)}') #내장 함수 min,max 사용