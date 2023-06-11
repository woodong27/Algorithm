from pprint import pprint
board = [list(map(int,input().split())) for _ in range(5)]
MC = [list(map(int,input().split())) for _ in range(5)]

di = [0,1,1,1]
dj = [1,-1,0,1]

def bingo():
    global bingo_cnt
    bingo_cnt = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 0:
                for k in range(4):
                    num_cnt = 0
                    for l in range(5): #범위 지정
                        dx = i + di[k]*l
                        dy = j + dj[k]*l

                        if 0 <= dx < 5 and 0 <= dy < 5 and board[dx][dy]==0:
                            num_cnt += 1
                                # print("확인",num_cnt,dx,dy)
                        if num_cnt == 5:
                            bingo_cnt += 1
                                    # print(i, j, "여기서", bingo_cnt)
            # if bingo_cnt != 3:
            #     bingo_cnt = 0
                                    # print("빙고",i,j,bingo_cnt)

flag = 0

ans=0
for i in range(5):
    for j in range(5):
        num = MC[i][j]
        for k in range(5):
            for l in range(5):
                if board[k][l] == num:
                    board[k][l] = 0
                    bingo()
                    ans+=1
                    if bingo_cnt >= 3:
                        print(ans)
                        flag = 1
                        break

                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 1:
        break