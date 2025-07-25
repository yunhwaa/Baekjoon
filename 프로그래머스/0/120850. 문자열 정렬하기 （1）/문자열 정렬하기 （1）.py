def solution(my_string):
    answer = []
    for s in my_string:
        if s.isdigit() == True:
            answer.append(int(s))
    answer = sorted(answer)
    return answer