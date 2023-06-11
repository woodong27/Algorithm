n=int(input())
list=[[int(x) for x in input().split()] for row in range(n)]
for i in range(n):
    print(f'#{i+1}',round(sum(list[i])/10))