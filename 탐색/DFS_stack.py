def dfs_stack(graph,start,goal):
    visited=[0]*(V+1)
    stack=[]
    stack.append(start)

    while stack: #더이상 방문할 노드가 없어서 스택이 빌때까지 반복
        now=stack.pop()
        if visited[now]==0: #현재 노드가 방문한적 없는 노드라면
            visited[now]=1 #visited를 1로 만들어주고 계속해서 탐색하기 위해 자식노드를 stack에 넣어줌
            stack.extend(graph[now]) #extend를 사용해서 자식노드가 2개 이상일 때 스택에 동시에 모두 넣어주고 탐색

    return visited[goal] #탐색이 끝났을 때 목표 노드를 방문했다면 1, 못했다면 0이 반환됨

V,E=map(int,input().split()) #V:노드의 수, E:노드간 연결의 수

graph=[[]for _ in range(V+1)] #0번 노드~V번째 노드까지 받을 그래프
for i in range(E):
    v1,v2=map(int,input().split()) #v1:부모->v2:자식
    graph[v1].append(v2) #그래프의 v1번째 인덱스에 그 자식인 v2를 넣어서 관계를 표시해줌
    # graph[v2].append(v1) #만약 단방향 그래프가 아니라 양방향 그래프면 v2의 자식에도 v1이 있음

S,G=map(int,input().split()) #S:탐색을 시작할 노드, E:탐색하려는 목표 노드

print(dfs_stack(graph,S,G))
