lst=[5,5,1,0,2,2,4,3,5,3]

counts=[0]*(max(lst)+1)
sorted_lst=[0]*(len(lst))

for i in lst:
    counts[i]+=1

print('첫 counts(0~5의 갯수) :', counts)
print()

for i in range(1,len(counts)):
    counts[i]+=counts[i-1]

print('변화된 counts(0~5를 넣기위한 index) :',counts)
print()
print('정렬 전 :',lst)
for i in lst:
    counts[i]-=1
    sorted_lst[counts[i]]=i
    print('counts의 변화 :',counts)
    print('lst의 인덱스 순서대로 sorted_lst에 추가되는 과정 :',sorted_lst)


print()
print('최종 정렬 결과 :',sorted_lst)