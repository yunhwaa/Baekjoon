def solution(start_num, end_num):
    answer = []
    for n in range(start_num, end_num-1, -1):
        answer.append(n)
    return answer