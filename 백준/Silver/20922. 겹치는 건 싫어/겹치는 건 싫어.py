# BOJ 20922 S1 겹치는 건 싫어

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

counts = [0] * (max(numbers) + 1)

answer, end = 0, 0
for start in range(n - k + 1):
    while end < n:
        if counts[numbers[end]] >= k:
            break
        counts[numbers[end]] += 1
        end += 1
    answer = max(answer, end - start)
    counts[numbers[start]] -= 1

print(answer)
