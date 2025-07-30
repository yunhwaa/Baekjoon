def solution(myString):
    answer = []
    string = myString.split('x')
    for s in string:
        answer.append(len(s))
    return answer