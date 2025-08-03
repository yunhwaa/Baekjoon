def solution(date1, date2):
    answer = 0

    for d1, d2 in zip(date1, date2):
        if d1 < d2:
            answer = 1
            break
        elif d1 > d2:
            answer = 0
            break
    return answer