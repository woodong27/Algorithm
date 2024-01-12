# 프로그래머스 lv2 두 원 사이의 정수 쌍

import math

def solution(r1, r2):
    answer = 0
    
    '''
    r1과 r2의 범위가 1에서 100만까지이기 때문에
    이중 반복문으로 전체를 조회하면 시간초과 발생
    -> 하나의 사분면에서 계산해서 결과에 곱하기 4를 한다면..?
    => 그렇게 해도 시간초과 발생..
    
    -> 이중반복문 대신에 원의 공식 이용
    x^2 + y^2 = r^2
    y = sqrt(r^2 - x^2)
    해당 공식을 사용하면 이중반복문을 쓰지 않고 y좌표(==i)만 주어졌을 때 x(==j)를 구할 수 있음
    '''
    
    # 1. x, y축 위에 있는 좌표 찾기
    temp1 = r2 - r1 + 1
    answer += temp1 * 4
    
    # 2. 제 1 사분면 위에 있는 좌표들 찾기
    temp2 = 0
    for i in range(1, r2):
        # 1. i가 r1보다 작을 때
        # i를 사용해서 r1에서의 j좌표를 구한 뒤
        # r1의 j좌표보다 크고 r2의 j좌표보다 작은 점들을 세어주면 됨
        if i < r1:
            r1_j = math.sqrt(r1 ** 2 - i ** 2)
            r1_j = math.ceil(r1_j)
            r2_j = math.sqrt(r2 ** 2 - i ** 2)
            r2_j = math.floor(r2_j)
            temp2 += r2_j - r1_j + 1
        
        # 2. i가 r1보다 클 때
        # i를 사용해서 r2의 j좌표를 구한 뒤
        # 1과 r2의 j좌표 사이에 있는 점들을 세어주면 됨
        else:
            r2_j = math.sqrt(r2 ** 2 - i ** 2)
            r2_j = math.floor(r2_j)
            temp2 += r2_j - 1 + 1
        
    # 제 1사분면에서 구한 점의 수에 4를 곱하면 전체 사분면에서의 좌표의 갯수
    answer += temp2 * 4
    
    return answer