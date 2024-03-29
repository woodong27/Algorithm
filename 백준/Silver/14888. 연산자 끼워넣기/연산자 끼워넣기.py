N=int(input())
numbers=list(map(str,input().split()))
temp=list(map(int,input().split()))

ops={0:'+',1:'-',2:'*',3:'/'}

op=[]
for i in range(4):
    if temp[i]!=0:
        for j in range(temp[i]):
            op.append(ops[i])

from itertools import permutations as perm
op_sets=list(perm(op))

from collections import deque

result=[]
for i in range(len(op_sets)):
    case=list(op_sets.pop())
    tlst=deque([])
    for j in range(N):
        tlst.append(numbers[j])
        if case:
            tlst.append(case.pop())

    temprlt=[]
    while tlst:
        if tlst[0].isdigit():
            temprlt.append(int(tlst.popleft()))
        else:
            oper=tlst.popleft()
            if oper=='+':
                temprlt.append(temprlt.pop()+int(tlst.popleft()))
            elif oper=='*':
                temprlt.append(temprlt.pop()*int(tlst.popleft()))
            elif oper=='-':
                temprlt.append(temprlt.pop()-int(tlst.popleft()))
            elif oper=='/':
                if temprlt[-1]<0:
                    temprlt.append(-((-temprlt.pop())//int(tlst.popleft())))
                else:
                    temprlt.append(temprlt.pop()//int(tlst.popleft()))

    result.append(*temprlt)

print(max(result))
print(min(result))