T=int(input())

for tc in range(T):
    N=int(input())

    ans=-1
    for i in range(1,1000001):
        if i**3==N:
            ans=i
            break

    print(f'#{tc+1} {ans}')