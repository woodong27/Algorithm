# BOJ 2559 S3 수열

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

end, temp = 0, 0
answer = -100 * k  # 최악의 경우
for start in range(n - k + 1):
    while end <= n:
        if end - start == k:
            answer = max(answer, temp)
            temp -= numbers[start]
            break
        temp += numbers[end]
        end += 1

print(answer)
