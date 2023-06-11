from collections import deque

N,K=map(int,input().split())

visited=[0]*100001
visited[N]=1
q=deque([(N,0)])
ans=abs(K-N)
while q:
    current,cnt=q.popleft()
    visited[current]=1
    if current==K:
        if ans>cnt:
            ans=cnt
    if cnt+1<ans:
        for nextp in [current+1,current-1]:
            if 0<=nextp<=100000:
                if not visited[nextp]:
                    q.append((nextp,cnt+1))
    if 0<=current*2<=100000 and not visited[current*2]:
        q.append((current*2,cnt))

print(ans)