# BOJ 14644 S5 욱제는 결정장애야!

n = int(input())
menus = list(map(int, input().split()))

board = [0] * (n + 1)

answer, count = 0, 0
for menu in menus:
    if not board[menu]:
        count += 1
        board[menu] = 1
    else:
        count -= 1

    answer = max(answer, count)

print(answer)
