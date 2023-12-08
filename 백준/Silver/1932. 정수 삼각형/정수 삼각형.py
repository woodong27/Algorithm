# 1932. 정수 삼각형

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(0, i + 1):
        if j == 0:
            triangle[i][0] += triangle[i - 1][0]
        elif j == i:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

answer = max(triangle[N - 1])
print(answer)
