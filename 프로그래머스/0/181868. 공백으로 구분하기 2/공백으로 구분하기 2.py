def solution(my_string):
    answer = []
    string = my_string.split(' ')
    for s in string:
        if len(s) != 0:
            answer.append(s)
    return answer