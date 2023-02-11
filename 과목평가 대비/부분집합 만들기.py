from pprint import pprint

lst = [-2,-1,1,2]

cnt = 0
subset = []
for i in range(1 << len(lst)):
    temp = []
    for j in range(len(lst)):
        if i & (1 << j):
            temp.append(lst[j]) #temp리스트에 숫자를 append해서 부분집합의 리스트를 만들고
    subset.append(temp) #temp리스트를 subset리스트에 넣어서 부분집합의 모음을 만듬
    if sum(temp) == 0:
        cnt += 1

print(cnt)  # 합이 0이 되는 부분집합의 갯수
pprint(subset)  # 만들어진 부분집합들
print(len(subset))  # 부분집합의 갯수 = 2^9=512개
