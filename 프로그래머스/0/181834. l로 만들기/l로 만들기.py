def solution(myString):
    answer = ''
    for s in myString:
        if str(s) < str('l'):
            s = 'l'
            answer += s
        else:
            answer += s
    return answer