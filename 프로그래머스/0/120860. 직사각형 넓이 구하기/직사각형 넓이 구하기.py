def solution(dots):
    answer = 0
    x, y = dots[0][0], dots[0][1]
    for d in dots:
        if d[0] != x:
            a = abs(x - d[0])
        
        if d[1] != y:
            b = abs(y - d[1])
    answer = a * b
    return answer