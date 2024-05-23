# BOJ 11660 S1 구간 합 구하기 5

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    board = [list(map(int, enter().split()))for _ in range(n)]

    dp = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + board[i-1][j-1]

    for _ in range(m):
        si, sj, ei, ej = map(int, enter().split())
        answer = dp[ei][ej] - dp[ei][sj-1] - dp[si-1][ej] + dp[si-1][sj-1]
        sys.stdout.write(f'{answer}\n')
