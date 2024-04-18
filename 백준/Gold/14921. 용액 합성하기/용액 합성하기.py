# BOJ 14921 G5 용액 합성하기

"""

"""

n = int(input())
solutions = list(map(int, input().split()))

start, end = 0, n - 1
answer = solutions[start] + solutions[end]
while end > start:
    temp = solutions[start] + solutions[end]
    if abs(temp) < abs(answer):
        answer = temp
    if temp < 0:
        start += 1
    else:
        end -= 1

print(answer)
