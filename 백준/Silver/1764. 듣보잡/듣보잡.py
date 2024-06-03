# BOJ 1764 S4 듣보잡

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())

    heard = set(enter().strip() for _ in range(n))
    seen = set(enter().strip() for _ in range(m))

    result = sorted(heard & seen)
    answer = '\n'.join(result)

    sys.stdout.write(f'{len(result)}\n')
    sys.stdout.write(f'{answer}\n')
