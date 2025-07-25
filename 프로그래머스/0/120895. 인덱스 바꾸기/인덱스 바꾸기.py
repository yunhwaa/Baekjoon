def solution(my_string, num1, num2):
    answer = ''
    for s in range(len(my_string)):
        if s == num1:
            answer += my_string[num2]
        elif s == num2:
            answer += my_string[num1]
        else:
            answer += my_string[s]
    return answer