def solution(myString):
    answer = []
    myString = myString.split('x')
    for s in myString:
        if len(s) != 0:
            answer.append(s)
    answer = sorted(answer)
    return answer