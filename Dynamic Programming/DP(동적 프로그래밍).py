'''
큰 문제를 작은 문제로 나누어서 작은문제에서 구한 정답을 계속해서 활용
'''

import time

#e.g : 피보나치 수열 구현
#재귀함수 사용 -> 입력되는 숫자가 커질수록 수행시간이 크게 증가
def fibo(x):
    if x<=2:
        return 1

    else:
        return fibo(x-1)+fibo(x-2)

for num in range(5,40,10):
    start=time.time()
    res=fibo(num)
    print('결과 :',res, ', x :',num, ', 러닝타임 : ',round(time.time()-start,2),'초')

print()

#다이나믹 프로그래밍 사용(Top-down) -> 수행시간이 매우 빠름
d=[0]*50

def fibo_dp(x):
    if x<=2:
        return 1

    if d[x]!=0:
        return d[x]
    else:
        d[x]=fibo_dp(x-1)+fibo_dp(x-2)

    return d[x]

for num in range(5,40,10):
    start=time.time()
    res=fibo_dp(num)
    print('결과 :',res, ', x :',num, ', 러닝타임 : ',round(time.time()-start,2),'초')

print()

#다이나믹 프로그래밍(Bottom-up)
dd=[0]*100

dd[1]=1
dd[2]=1
N=99

for i in range(3,N+1):
    dd[i]=dd[i-1]+dd[i-2]

print(dd[N])