def solution(myString, pat):
    answer = 0
    string = ''
    for s in myString:
        if s == "A":
            string += 'B'
        elif s == "B":
            string += 'A'
    
    if pat in string:
        answer = 1
            
    return answer