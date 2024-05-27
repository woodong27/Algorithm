# BOJ 1620 S4 나는야 포켓몬 마스터 이다솜

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    pokemons = {i + 1: enter().strip() for i in range(n)}
    reverse = {value: key for key, value in pokemons.items()}

    for _ in range(m):
        quest = enter().strip()
        try:
            quest = int(quest)
            sys.stdout.write(f'{pokemons[quest]}\n')
        except ValueError:
            quest = quest
            sys.stdout.write(f'{reverse[quest]}\n')
