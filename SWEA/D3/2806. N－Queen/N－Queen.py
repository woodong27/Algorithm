def is_promising(i,j):
    for ii in range(N):
        if abs(col[ii]-j)==abs(ii-i) and board[ii][col[ii]]==1:
            return False

    return True

def backtrack(i):
    global ans
    if i==N:
        ans+=1
        return

    for j in range(N):
        if not row[j]:
            if is_promising(i,j):
                row[j]=1
                col[i]=j
                board[i][j]=1
                backtrack(i+1)
                row[j]=0
                col[i]=0
                board[i][j]=0

T=int(input())

for tc in range(T):
    N=int(input())
    board=[[0]*N for _ in range(N)]
    row=[0]*N
    col=[0]*N

    ans=0
    backtrack(0)
    print(f'#{tc+1} {ans}')