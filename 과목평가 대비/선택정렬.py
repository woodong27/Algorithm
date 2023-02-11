lst=[6,4,5,2,1,7,8,3,10,9]

#최소값의 인덱스만 기억해서 마지막에 한번에 바꾸는 방법
for i in range(10):
    min_idx=i
    for j in range(i+1,10):
        if lst[min_idx]>lst[j]:
            min_idx=j
            print('최소값의 인덱스, 해당 인덱스의 값 :',min_idx,',' ,lst[min_idx])
    lst[i],lst[min_idx]=lst[min_idx],lst[i]
    print(f'{min_idx}번째 위치의 값인 {lst[min_idx]}와 {i}번째 인덱스의 {lst[i]}가 바뀜')
    print(lst)
    print()


#내가 했던 방법
# for i in range(10):
#     for j in range(i+1,10):
#         if lst[i]>lst[j]:
#             lst[i],lst[j]=lst[j],lst[i]
#     print(lst)

