from collections import deque

N,K=map(int,input().split())

visited=[0]*100001
visited[N]=1
q=deque([(N,0)])
min_cnt=abs(N-K)
ans=0
while q:
    current,cnt=q.popleft()
    visited[current]=1
    if current==K:
        if min_cnt>=cnt:
            min_cnt=cnt
            ans+=1
    for nextp in [current+1,current-1,current*2]:
        if 0<=nextp<=100000:
            if not visited[nextp]:
                q.append((nextp,cnt+1))
            elif nextp==K and min_cnt-1==cnt:
                ans+=1

print(min_cnt)
print(ans)