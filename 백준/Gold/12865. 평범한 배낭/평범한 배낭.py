# BOJ 12865 G5 평범한 배낭

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, k = map(int, enter().split())
    bag = [list(map(int, enter().split())) for _ in range(n)]

    dp = [[0 for _ in range(k + 1)]for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if bag[i-1][0] <= j:
                dp[i][j] = max(bag[i-1][1] + dp[i-1][j-bag[i-1][0]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    sys.stdout.write(f'{dp[n][k]}\n')
