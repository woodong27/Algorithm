lst=[6,4,5,2,1,7,8,3,10,9]

for i in range(10):
    for j in range(9):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            print(lst)
