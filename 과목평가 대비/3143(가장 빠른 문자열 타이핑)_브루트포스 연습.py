T=int(input())

for x in range(T):
    A,B=map(str,input().split())

    #A에서 B가 몇개 있는지 찾기
    a=len(A)
    i=0 #A의 인덱스

    b=len(B)
    j=0 #B의 인덱스

    count=0

    #1. A[i]와 B[j]가 다를때만 조건을 넣어주는 방법
    '''
    while i<a and j<b:
        if A[i]!=B[j]:
            i=i-j
            j=-1
        i+=1
        j+=1

        if j==b:
            count+=1
            j=0
    '''

    #2. A[i]와 B[j]가 같을때와 다를 때 두가지 조건을 넣어준 방법
    while i<a and j<b:
        if A[i]==B[j]:
            i+=1
            j+=1
        else:
            i=i-j+1
            j=0

        if j==b:
            count+=1
            j=0

    print(f'#{x+1} {a-count*b+count}')