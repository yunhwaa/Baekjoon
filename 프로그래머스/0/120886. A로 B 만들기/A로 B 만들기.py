def solution(before, after):
    answer = 0
    b_list = list(set(before))
    for b in b_list:
        if before.count(b) == after.count(b):
            answer = 1
        else:
            answer = 0
            break
    return answer