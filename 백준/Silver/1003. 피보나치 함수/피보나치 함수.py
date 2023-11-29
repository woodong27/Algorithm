# 1003. 피보나치 함수

T = int(input())

while T:
    T -= 1

    N = int(input())
    dp0 = [0] * (N + 1)
    dp1 = [0] * (N + 1)
    if N < 4:
        dp0 = [0] * 4
        dp1 = [0] * 4

    dp0[0], dp0[1], dp0[2], dp0[3] = 1, 0, 1, 1
    dp1[0], dp1[1], dp1[2], dp1[3] = 0, 1, 1, 2

    for i in range(4, N + 1):
        dp0[i] = dp0[i - 1] + dp0[i - 2]
        dp1[i] = dp1[i - 1] + dp1[i - 2]

    print(dp0[N], dp1[N])
