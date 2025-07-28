def solution(my_str, n):
    answer = []
    for s in range(0, len(my_str), n):
        answer.append(my_str[s:s+n])
    return answer