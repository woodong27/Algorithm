# BOJ 2493 G5 탑

n = int(input())
towers = list(map(int, input().split()))

answer = [0] * n
stack = [n-1]

for i in range(n-1, -1, -1):
    while stack and towers[i] > towers[stack[-1]]:
        answer[stack.pop()] = i + 1
    stack.append(i)

print(*answer, sep=" ")
