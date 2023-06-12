T = int(input())
for test_case in range(1, T + 1):

    N = int(input())
    ai = input()
    aii = int(ai)
    list_a = [0]*10

    for i in range(len(str(ai))):
        list_a[aii % 10] +=1
        aii //= 10
    count_zero = 0

    for i in range(len(ai)):
        if ai[i] == '0':
            count_zero += 1

    list_a[0] = count_zero

    maxv , max_num = 0, 0
    for i in range(-1,-11,-1):
        if list_a[i] > maxv:
            maxv = list_a[i]
            max_num = i +10
#            print(max_num)
  #  print(maxv , max_num)
    print(f"#{test_case} {max_num} {maxv}")