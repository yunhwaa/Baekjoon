def solution(quiz):
    answer = []
    for q in quiz:
        q_list = q.split(' ')
        if q_list[1] == "+":
            if int(q_list[0]) + int(q_list[2]) == int(q_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif q_list[1] == "-":
            if int(q_list[0]) - int(q_list[2]) == int(q_list[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer