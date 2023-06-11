def inorder(node):
    if node<N+1:
        inorder(node*2)
        print(tree[node],end='')
        inorder(node*2+1)

for tc in range(10):
    N=int(input()) #트리의 노드의 수

    tree=[0]*(N+1)
    for i in range(N):
        lst=list(input().split())
        tree[i+1]=lst[1]

    print(f'#{tc+1}',end=' ')
    inorder(1)
    print()