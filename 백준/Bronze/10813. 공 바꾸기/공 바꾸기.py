# BOJ 10813 B2 공 바꾸기

n, m = map(int, input().split())
baskets = [i for i in range(n + 1)]

for _ in range(m):
    from_, to = map(int, input().split())
    baskets[from_], baskets[to] = baskets[to], baskets[from_]

print(*baskets[1:])
