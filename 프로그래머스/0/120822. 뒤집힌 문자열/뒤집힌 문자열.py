def solution(my_string):
    answer = ''
    for s in range(1, len(my_string)+1):
        answer += my_string[-s]
    return answer