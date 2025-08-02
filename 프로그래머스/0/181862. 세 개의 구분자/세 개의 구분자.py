def solution(myStr):
    answer = []
    st = ''
    for s in myStr:
        if s == "a" or s == "b" or s == "c":
            if len(st) != 0:
                answer.append(st)
                st = ''
        else:
            st += s
    if len(st) > 0:
        answer.append(st)
    elif len(answer) == 0:
        answer.append("EMPTY")
    return answer