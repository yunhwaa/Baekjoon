def solution(n):
    answer = 1
    num = 1
    while answer <= n:
        answer *= num
        num += 1
    
    return num - 2