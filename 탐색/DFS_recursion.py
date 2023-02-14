def dfs_recursion(graph,start_node,end_node):
    visited[start_node]=1

    for i in range(1,V+1):
        if i in graph[start_node] and not visited[i]:
            dfs_recursion(graph,i,end_node)

V,E=map(int,input().split())
visited=[0]*(V+1)

graph=[[]for _ in range(V+1)]
for i in range(E):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    # graph[v2].append(v1) # 양방향 그래프일때

S,G=map(int,input().split())

dfs_recursion(graph,S,G)

print(visited[G])