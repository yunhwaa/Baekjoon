def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    for key in keyinput:
        if key == "left":
            x -= 1
            if x < (board[0]//2) * -1:
                x = (board[0]//2) * -1 
        elif key == "right":
            x += 1
            if x > (board[0]//2):
                x = (board[0]//2) 
        elif key == "up":
            y += 1
            if y > (board[1]//2):
                y = (board[1] // 2) 
        elif key == "down":
            y -= 1
            if y < (board[1]//2)*-1:
                y = (board[1]//2)*-1 
    answer.append(x)
    answer.append(y)
    return answer