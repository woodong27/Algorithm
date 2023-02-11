lst1=[[1,2,3],[4,5,6],[7,8,9]]

print('행 우선 탐색')
for i in range(len(lst1)):
    for j in range(len(lst1[i])):
        print(lst1[i][j], end=' ')
print('\n')

print('열 우선 탐색')
for x in range(len(lst1)):
    for y in range(len(lst1[i])):
        print(lst1[y][x],end=' ')
print('\n')

from pprint import pprint

print('2차원 배열 전치하기(행, 열 바꾸기)')

#2중 반복문으로 행렬 전치하기
print('방법 1')
lst2=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print('전치 전')
pprint(lst2)

for a in range(len(lst2)):
    for b in range(len(lst2[i])):
        if a<b:
            lst2[a][b],lst2[b][a]=lst2[b][a],lst2[a][b]
print('전치 후')
pprint(lst2)

print()

#zip과 *(unpacking)을 사용해서 전치하기
print('방법 2')
lst3=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

print('전치 전')
pprint(lst3)

lst3=list(map(list,zip(*lst3)))
print('전치 후')
pprint(lst3)
