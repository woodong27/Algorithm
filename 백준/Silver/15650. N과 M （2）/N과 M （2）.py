# 15650. N과 M(2)

N, M = map(int, input().split())
answer = []

# dfs로 해결
def dfs(start):
    global answer
    if len(answer) == M:
        print(*answer)
        return

    for i in range(start, N + 1):
        if i not in answer:
            answer.append(i)
            dfs(i + 1)
            answer.pop()

dfs(1)
