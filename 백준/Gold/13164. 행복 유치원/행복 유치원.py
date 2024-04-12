# BOJ 13164 G5 행복 유치원

N, K = map(int, input().split())
children = list(map(int, input().split()))

difference = [children[i] - children[i-1] for i in range(1, N)]
difference.sort()

answer = sum(difference[:N-K])
print(answer)
