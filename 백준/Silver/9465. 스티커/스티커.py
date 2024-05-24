# BOJ 9465 S1 스티커

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    t = int(enter())
    for _ in range(t):
        n = int(enter())
        scores = [list(map(int, enter().split()))for _ in range(2)]

        if n == 1:
            sys.stdout.write(f'{max(scores[0][0], scores[1][0])}\n')
            continue

        dp = [[0] * n for _ in range(2)]
        dp[0][0] = scores[0][0]
        dp[1][0] = scores[1][0]

        dp[0][1] = scores[1][0] + scores[0][1]
        dp[1][1] = scores[0][0] + scores[1][1]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + scores[0][i]
            dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + scores[1][i]

        sys.stdout.write(f'{max(dp[0][n-1], dp[1][n-1])}\n')
