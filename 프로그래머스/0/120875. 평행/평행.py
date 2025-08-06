def solution(dots):
    answer = 0
    x1, x2, x3, x4 = dots[0][0], dots[1][0], dots[2][0], dots[3][0]
    y1, y2, y3, y4 = dots[0][1], dots[1][1], dots[2][1], dots[3][1]
    if (x2 - x1) * (y4 - y3) == (x4 - x3) * (y2 - y1):
        answer = 1
    elif (x3 - x1) * (y4 - y2) == (x4 - x2) * (y3 - y1):
        answer = 1
    elif (x4 - x1) * (y3 - y2) == (x3 - x2) * (y4 - y1):
        answer = 1
    else:
        answer = 0
    return answer

