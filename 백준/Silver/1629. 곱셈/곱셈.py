# 1629. 곱셈

A, B, C = map(int, input().split())

# 나머지 분배 법칙
'''
(AxB)%C = (A%C) *(B%C) % C
'''

# 예제에 적용
'''
a = 10 , b = 11 , c = 12
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
'''


def calculating(a, b, c):
    if b == 1:
        return a % c
    else:
        temp = calculating(a, b // 2, c)
        if not b % 2:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


answer = calculating(A, B, C)

print(answer)
