T=int(input())

def quick_sort(lst):
    if len(lst)<2:
        return lst

    pivot=lst[0]
    leftover=lst[1:]
    left,right=[],[]
    for num in leftover:
        if num<=pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left)+[pivot]+quick_sort(right)

for tc in range(T):
    N=int(input())
    numbers=list(map(int,input().split()))

    result=quick_sort(numbers)
    print(f'#{tc+1} {result[N//2]}')