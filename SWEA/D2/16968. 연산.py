from collections import deque

T=int(input())

def operating(num,selection):
    if selection==0:
        num+=1
    elif selection==1:
        num-=1
    elif selection==2:
        num*=2
    else:
        num-=10

    return num

def calculating(n):
    q=deque([(n,0)])
    while q:
        current,cnt=q.popleft()
        if current==M:
            return cnt
        for i in range(4):
            operated_n=operating(current,i)
            if 0<operated_n<=1000000 and not visited[operated_n]:
                visited[operated_n]=1
                q.append((operated_n,cnt+1))

for tc in range(T):
    N,M=map(int,input().split())

    visited=[0]*1000001
    visited[N]=1
    ans=calculating(N)

    print(f'#{tc+1}',ans)