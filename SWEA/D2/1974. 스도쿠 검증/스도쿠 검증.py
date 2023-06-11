T=int(input())

def check(lst):
    for i in range(9):
        sum_col=0
        sum_row=0
        for j in range(9):
            sum_col+=lst[i][j]
            sum_row+=lst[j][i]
        if sum_col!=45:
            return 0
        if sum_row!=45:
            return 0

    return 1

def check_sqaure(lst):
    for i in range(0,9,3):
        for j in range(0,9,3):
            sum=0
            for k in range(3):
                for l in range(3):
                    sum+=lst[i+k][j+l]
            if sum!=45:
                return 0

    return 1

for x in range(T):
    lst=[list(map(int,input().split()))for _ in range(9)]

    ans=check(lst)
    if ans==1:
        ans=check_sqaure(lst)

    print(f'#{x+1} {ans}')