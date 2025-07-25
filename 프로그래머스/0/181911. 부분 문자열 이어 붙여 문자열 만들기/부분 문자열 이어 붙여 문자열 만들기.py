def solution(my_strings, parts):
    answer = ''
    for s, p in zip(my_strings, parts):
        str = s[p[0]:p[1]+1]
        answer += str
    return answer