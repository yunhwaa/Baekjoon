def solution(myString):
    answer = myString.replace('a', 'A')
    for a in answer:
        if a != "A":
            answer = answer.replace(a, a.lower())
    return answer