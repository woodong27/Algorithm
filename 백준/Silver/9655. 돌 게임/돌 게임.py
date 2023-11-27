# 9655. 돌 게임

import sys

# N개의 돌
N = int(sys.stdin.readline().strip())

dp = [''] * (N + 1)
if N < 4:
    dp = [''] * 4

dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'

# n - 1이나 n - 3이 존재하면 그 반대가 우승하게 되는 게임
for i in range(4, N + 1):
    if dp[i-1] == 'SK' or dp[i-3] == 'SK':
        dp[i] = 'CY'
    else:
        dp[i] = 'SK'

print(dp[N])

# or N이 짝수면 CY, 홀수면 SK가 이기는 게임
