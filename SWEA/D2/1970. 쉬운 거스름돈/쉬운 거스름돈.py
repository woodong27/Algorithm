T=int(input())

moneys=[50000,10000,5000,1000,500,100,50,10]

for tc in range(T):
    N=int(input())
    ans=[0]*8

    for i in range(8):
        if N>=moneys[i]:
            ans[i]+=N//moneys[i]
            N%=moneys[i]

    print(f'#{tc+1}')
    print(*ans)