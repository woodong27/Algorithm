# 5073. 삼각형과 세 변

import sys

while True:
    numbers = list(map(int, sys.stdin.readline().strip().split()))

    if not sum(numbers):
        break
    else:
        numbers.sort()
        if numbers[2] >= numbers[1] + numbers[0]:
            print('Invalid')
        else:
            if numbers.count(numbers[2]) == 3:
                print('Equilateral')
            elif numbers.count(numbers[2]) == 2 or numbers[0] == numbers[1]:
                print('Isosceles')
            else:
                print('Scalene')
