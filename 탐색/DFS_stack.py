def dfs_stack(graph,start,goal):
    # 인접 행렬
    # stack=[]
    # stack.append(start)
    # while stack:
    #     now=stack.pop()
    #     if visited[now]==0:
    #         visited[now]=1
    #         for i in range(V+1):
    #             if graph[now][i]==1:
    #                 stack.append(i)

    # 인접리스트
    stack=[]
    stack.append(start)
    while stack: #더이상 방문할 노드가 없어서 스택이 빌때까지 반복
        now=stack.pop()
        if visited[now]==0: #현재 노드가 방문한적 없는 노드라면
            visited[now]=1 #visited를 1로 만들어주고 계속해서 탐색하기 위해 자식노드를 stack에 넣어줌
            for i in graph[now]:
                stack.append(i) #자식노드들을 stack에 push해서 계속 탐색
            # 다른 방법
            # stack.extend(graph[now]) #extend를 사용하면 스택에 자식노드를 한번에 append해줄 수 있음

    '''
    만약 더이상 자식 노드가 없으면 stack에 더이상 값이 추가되지 않아
    스택의 pop이 계속되다가 스택이 비게 되면 탐색 종료
    '''
    return visited[goal] #탐색이 끝났을 때 목표 노드를 방문했다면 1, 못했다면 0이 반환됨

V,E=map(int,input().split()) #V:노드의 수, E:노드간 연결의 수

graph=[[]for _ in range(V+1)] #0번 노드~V번째 노드까지 받을 그래프(인접리스트)
graph2=[[0 for _ in range(V+1)]for _ in range(V+1)] #인접 행렬
for i in range(E):
    v1,v2=map(int,input().split()) #v1:부모->v2:자식
    graph[v1].append(v2) #그래프의 v1번째 인덱스에 그 자식인 v2를 넣어서 관계를 표시해줌
    # graph[v2].append(v1) #만약 단방향 그래프가 아니라 양방향 그래프면 v2의 자식에도 v1이 있음

    #인접행렬
    graph2[v1][v2]=1
    # graph[v2][v1]=1

S,G=map(int,input().split()) #S:탐색을 시작할 노드, G:탐색하려는 목표 노드

visited=[0]*(V+1) #visited 리스트는 함수 안/밖 어디있든 상관없음

print(dfs_stack(graph,S,G)) #인접리스트로 했을때 결과
# print(dfs_stack(graph2,S,G)) #인접행렬로 했을때 결과

'''
input 예시
6 5
1 4
1 3
2 3
2 5
4 6
1 6

S,G=1,6으로
1번 노드에서 탐색을 시작하면 6번노드를 방문하기 때문에 결과가 1이 나옴
'''