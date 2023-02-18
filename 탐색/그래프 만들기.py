V,E=map(int,input().split()) #V:노드의 갯수, E:간선의 갯수

#인접 배열
graph=[[0 for _ in range(V+1)]for _ in range(V+1)] #0~V번까지의 노드 표현
#인접리스트
graph2=[[]for _ in range(V+1)]

for i in range(E): #간선의 갯수 만큼 부모-자식 관계 입력받음
    v1,v2=map(int,input().split()) #v1:부모, v2:자식

    '''
    그래프의 행을 부모, 열을 자식으로 생각해서
    v1에 연결된 자식들은 v1행의 v2열에 1로 표시해준다.
    '''
    graph[v1][v2]=1
    # graph[v2][v1]=1 #만약 양방향 그래프라면 서로가 서로의 부모-자식이 되기 때문에 해줘야함


    '''
    그래프의 v1번째 인덱스의 리스트에 v2를 append해서 자식임을 표현해줌
    '''
    graph2[v1].append(v2)
    # graph2[v2].append(v1) #양방향 그래프라면 해줘야함

from pprint import pprint
pprint(graph)
print()
pprint(graph2)
'''
input 예시
6 5
1 4
1 3
2 3
2 5
4 6

출력 결과
인접행렬
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 1, 0, 0],
 [0, 0, 0, 1, 0, 1, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
 
인접리스트
[[], [4, 3], [3, 5], [], [6], [], []]
'''