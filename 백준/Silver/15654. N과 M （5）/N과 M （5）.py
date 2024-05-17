# BOJ 15654 S3 N과 M(5)

def backtracking(list_):
    if len(list_) == m:
        print(*list_)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            backtracking(list_ + [numbers[i]])
            visited[i] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    numbers.sort()
    visited = [0] * n
    for i in range(n):
        visited[i] = 1
        backtracking([numbers[i]])
        visited[i] = 0
