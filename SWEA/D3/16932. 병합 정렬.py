T=int(input())

def merge_sort(lst):
    global cnt
    if len(lst)<2:
        return lst

    m=len(lst)//2
    left=merge_sort(lst[:m])
    right=merge_sort(lst[m:])

    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result+=left[i:]
    result+=right[j:]
    if left[-1]>right[-1]:
        cnt+=1

    return result

for tc in range(T):
    N=int(input())
    numbers=list(map(int,input().split()))

    cnt=0
    sorted_numbers=merge_sort(numbers)
    print(f'#{tc+1} {sorted_numbers[N//2]} {cnt}')