# BOJ 1541 S2 잃어버린 괄호

"""
수식을 계산했을 때 가장 작은 결과를 반환하도록 해야한다.
-를 기준으로 식들을 나눠서, 가장 마지막에 - 연산을 진행하면 된다.
"""

formula = input()

bracketed_with_minus = formula.split('-')
result = []
for numbers_with_plus in bracketed_with_minus:
    temp = 0
    numbers = numbers_with_plus.split('+')
    for number in numbers:
        temp += int(number)

    result.append(temp)

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)
