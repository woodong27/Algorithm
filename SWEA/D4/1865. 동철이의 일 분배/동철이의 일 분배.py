T=int(input())

def assign_work(i,mulv):
    global ans
    if i==N:
        if ans<mulv:
            ans=mulv
        return

    if ans>=mulv:
        return

    for j in range(N):
        if not assigned[j]:
            assigned[j]=1
            assign_work(i+1,mulv*works[i][j])
            assigned[j]=0

for tc in range(T):
    N=int(input())
    works=[[int(i)/100 for i in input().split()]for _ in range(N)]
    assigned=[0]*N

    ans=0
    assign_work(0,1)
    ans*=100

    print(f'#{tc+1} %0.6f'%ans)