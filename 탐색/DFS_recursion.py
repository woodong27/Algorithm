def dfs_recursion(graph,start_node):
    visited[start_node]=1

    for i in range(1,V+1):
        if i in graph[start_node] and not visited[i]:
            dfs_recursion(graph,i)
            '''
            자식노드가 존재하면 자식노드로 이동해서 탐색
            더이상 자식노드가 나오지 않을때까지 반복
            '''

V,E=map(int,input().split())
visited=[0]*(V+1)

graph=[[]for _ in range(V+1)]
for i in range(E):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    # graph[v2].append(v1) # 양방향 그래프일때

S,G=map(int,input().split())

dfs_recursion(graph,S)

print(visited[G])

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