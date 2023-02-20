'''
N가지 종류의 화폐를 최소한으로 사용해서 가치의 합이 M원이 되도록 하려고 한다.
각 화폐는 몇개라도 사용할 수 있고, 순서가 달라도 구성이 같으면 같은 경우로 구분
첫째줄에 N,M (1<=N<=100, 1<=M<=10000)
이후 N개의 줄에 각 화폐의 가치가 주어짐(10000이하의 자연수)
첫째줄에 경우의 수 X를 출력
불가능할 때는 -1 출력
'''


'''
input
2 15
2
3
'''
N,M=map(int,input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))

dp=[0]+[10001]*M

print(coins)
print(dp)