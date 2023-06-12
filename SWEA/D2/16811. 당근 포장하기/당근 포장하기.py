T=int(input())

for tc in range(T):
    N=int(input())
    carrots=list(map(int,input().split()))
    carrots.sort()

    minv=1000
    for i in range(N-2): #소 박스에는 N-3까지
        for j in range(i+1,N-1): #중 박스에는 소 박수 이후~N-2까지
            if carrots[i]!=carrots[i+1] and carrots[j]!=carrots[j+1]: #같은 크기가 다른박스로 나눠지면 안됨
                s=i+1
                m=j-i
                b=N-1-j
                if 0<s<=N//2 and 0<m<=N//2 and 0<b<=N//2:
                    if minv>max(s,m,b)-min(s,m,b):
                        minv=max(s,m,b)-min(s,m,b)

    if minv==1000:
        minv=-1

    print(f'#{tc+1} {minv}')