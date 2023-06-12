T=int(input())

def heapify(n):
    heap.append(n)
    idx=len(heap)-1
    while idx>1:
        if heap[idx]<heap[idx//2]:
            heap[idx],heap[idx//2]=heap[idx//2],heap[idx]
        idx//=2


for tc in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    heap=[0]

    for i in lst:
        heapify(i)

    ans=0
    idx=N//2
    while idx:
        ans+=heap[idx]
        idx//=2

    print(f'#{tc+1} {ans}')