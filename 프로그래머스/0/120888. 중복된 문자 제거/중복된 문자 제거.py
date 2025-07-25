def solution(my_string):
    answer = ''
    ans_list = []
    for s in my_string:
        if s not in ans_list:
            answer += s
            ans_list.append(s)
    return answer