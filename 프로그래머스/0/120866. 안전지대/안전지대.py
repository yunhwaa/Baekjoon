def solution(board):
    danger = [[0] * len(board) for _ in range(len(board))]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                danger[i][j] = 1
                for d in range(8):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0 <= ni < len(board) and 0 <= nj < len(board):
                        danger[ni][nj] = 1
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if danger[i][j] == 0:
                count += 1
    return count 