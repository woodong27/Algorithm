# 2839. 설탕 배달

sugar = int(input())

# 필요한 봉지 수
bag = 0

while True:
    if sugar == 0:
        print(bag)
        break
    elif sugar < 0:
        print(-1)
        break

    # 설탕이 5의 배수일 경우
    if not sugar % 5:
        bag += sugar // 5
        print(bag)
        break
    # 설탕이 5의 배수가 될 때 까지 3을 빼줌
    else:
        sugar -= 3
        bag += 1
