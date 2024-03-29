# BOJ 1107 G5 리모컨

N = int(input())
M = int(input())
broken = list(input().split()) if M else []
start = 100

answer = abs(N - start)  # 최악의 경우(모두 +나 -버튼으로만 이동)
for i in range(1000001):  # 0 ~ 9번 버튼이 모두 고장나면 최악의 경우 10만부터 내려와야 한다.\
    number = str(i)
    for n in number:
        if broken and n in broken:
            break
    else:
        answer = min(answer, len(number) + abs(i - N))

print(answer)
