# BOJ 1764 S4 듣보잡

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    heard = [enter().strip() for _ in range(n)]
    seen = [enter().strip() for _ in range(m)]

    none = {}
    for person in heard:
        if person not in none.keys():
            none[person] = 1
        else:
            none[person] += 1

    for person in seen:
        if person not in none.keys():
            none[person] = 1
        else:
            none[person] += 1

    answer = sorted([key for key, value in none.items() if value >= 2])
    sys.stdout.write(f'{len(answer)}\n')
    sys.stdout.write('\n'.join(answer))
