def solution(my_string, s, e):
    answer = ''
    st = ''
    for i in range(s, e+1):
        st += my_string[i]
    answer += my_string[:s] + st[::-1] + my_string[e+1:]
    return answer