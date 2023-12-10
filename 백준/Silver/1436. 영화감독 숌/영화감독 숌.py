# 영화감독 숌

N = int(input())

count, answer = 0, 666

# 666부터 1씩 더해서 666이 있는 경우에만 count를 증가시킴
while True:
    if '666' in str(answer):
        count += 1
    
    # count와 N이 동일해지면 현재의 answer를 출력
    if count == N:
        break

    answer += 1

print(answer)
