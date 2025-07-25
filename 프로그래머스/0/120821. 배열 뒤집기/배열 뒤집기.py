def solution(num_list):
    answer = []
    for n in range(1, len(num_list)+1):
        answer.append(num_list[-n])
    return answer