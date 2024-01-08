def solution(board, h, w):
    answer = 0
    
    length = len(board[0])
    
    for di, dj in ((0,1), (0,-1), (-1,0), (1,0)):
        ni, nj = h + di, w + dj
        if 0 <= ni < length and 0<= nj < length:
            if board[ni][nj] == board[h][w]:
                answer += 1
                
    return answer