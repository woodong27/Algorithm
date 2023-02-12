'''
단순히 리스트의 처음부터 비교하며
찾으려고 하는 key값과 같은 원소가 있으면 탐색을 성공
정렬되어있지 않은 자료에서는 모든 원소를 비교해야하고
정렬되어있는 자료에서는 키값보다 원소가 커지면 탐색을 중단할 수 있음
'''
lst=[22,15,0,8,7,13,44,23]
key=13

#정렬 안된 자료
ans='실패'
cnt=0
for i in range(len(lst)):
    if lst[i]==key:
        ans='성공'
        break

print(ans)

#정렬 된 자료
for i in range(len(lst)):
    min_idx=i
    for j in range(i+1,len(lst)):
        if lst[min_idx]>lst[j]:
            min_idx=j
    lst[min_idx],lst[i]=lst[i],lst[min_idx]

ans='실패'
i=0
while i<len(lst) and lst[i]<=key:
    if lst[i]==key:
        ans='성공'
    i+=1

print(ans)