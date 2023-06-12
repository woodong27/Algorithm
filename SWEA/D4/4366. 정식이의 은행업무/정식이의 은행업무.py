T=int(input())

def bi_to_deci(numbers):
    result=0
    numbers.reverse()
    for i in range(len(numbers)):
        result+=numbers[i]*2**i

    return result

def ter_to_deci(numbers):
    result=0
    numbers.reverse()
    for i in range(len(numbers)):
        result+=numbers[i]*3**i

    return result

def comparing(bi,ter):
    global ans

    binaries=[]
    for i in range(len(bi)):
        copy2=bi[:]
        if copy2[i]:
            copy2[i]=0
        else:
            copy2[i]=1
        binaries.append(bi_to_deci(copy2))

    ternaries=[]
    for i in range(len(ter)):
        for j in range(3):
            copy3=ter[:]
            if j!=ter[i]:
                copy3[i]=j
                ternaries.append(ter_to_deci(copy3))

    for decimal in binaries:
        if decimal in ternaries:
            ans=decimal
            return

for tc in range(T):
    binary=list(map(int,input()))
    ternary=list(map(int,input()))

    ans=0
    comparing(binary,ternary)

    print(f'#{tc+1}', ans)