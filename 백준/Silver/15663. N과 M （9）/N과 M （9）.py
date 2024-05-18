# BOJ 15663 S2 N과 M(9)


def backtracking(list_):
    if len(list_) == m:
        temp = tuple(list_)
        if temp not in used:
            used.add(temp)
            print(*list_)
        return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            backtracking(list_ + [numbers[j]])
            visited[j] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    used = set()
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        backtracking([numbers[i]])
        visited[i] = 0
