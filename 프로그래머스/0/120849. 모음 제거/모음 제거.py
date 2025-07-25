def solution(my_string):
    answer = ''
    for s in my_string:
        if s != "a" and s != "e" and s != "i" and s != "o" and s != "u":
            answer += s
    return answer