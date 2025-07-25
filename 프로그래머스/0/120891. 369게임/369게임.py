def solution(order):
    answer = 0
    for n in str(order):
        if int(n) == 3 or int(n) == 6 or int(n) == 9:
            answer += 1
    return answer