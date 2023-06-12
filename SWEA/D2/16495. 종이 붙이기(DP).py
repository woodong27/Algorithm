T=int(input())

dp=[0]*301
dp[10]=1
dp[20]=3

for x in range(T):
    N=int(input())
    for i in range(30,N+1):
        if not i%10:
            dp[i]=dp[i-10]+2*dp[i-20]
    print(f'#{x+1} {dp[N]}')