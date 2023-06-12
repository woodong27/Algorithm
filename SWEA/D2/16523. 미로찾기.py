def dfs(graph,si,sj,gi,gj):
    stack=[]
    stack.append([si,sj])

    while stack:
        now=stack.pop()
        if visited[now[0]][now[1]]==0:
            visited[now[0]][now[1]]=1
            for i in range(4):
                if 0<=now[0]+di[i]<N and 0<=now[1]+dj[i]<N:
                    ni=now[0]+di[i]
                    nj=now[1]+dj[i]
                    if graph[ni][nj]!='1' and visited[ni][nj]!=1:
                        stack.append([ni,nj])

    return visited[gi][gj]

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

for x in range(T):
    N=int(input())

    maze=[list(input())for _ in range(N)]

    visited=[[0 for _ in range(N)]for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                si,sj=i,j
            elif maze[i][j]=='3':
                gi,gj=i,j

    print(f'#{x+1} {dfs(maze,si,sj,gi,gj)}')