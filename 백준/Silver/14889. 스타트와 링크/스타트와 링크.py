def calculate_synergy(lst1,lst2):
    synergy1,synergy2=0,0
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            synergy1+=synergies[lst1[i]][lst1[j]]

    for i in range(len(lst2)):
        for j in range(len(lst2)):
            synergy2+=synergies[lst2[i]][lst2[j]]

    return abs(synergy1-synergy2)

def cooking(i,dish1):
    global ans

    dish2=[]
    if len(dish1)==N//2:
        for i in range(N):
            if i not in dish1:
                dish2.append(i)
        difference=calculate_synergy(dish1,dish2)
        if difference<ans:
            ans=difference
        return

    for i in range(i,N):
        if not used[i]:
            used[i]=1
            dish1.append(i)
            cooking(i+1,dish1)
            used[i]=0
            dish1.pop()


N=int(input())
synergies=[list(map(int,input().split()))for _ in range(N)]

used=[1]+[0]*(N-1)
ans=20000*4-4
cooking(0,[0])
print(ans)