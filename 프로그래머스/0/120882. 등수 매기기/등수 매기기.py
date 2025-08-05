def solution(score):
    answer = [0] * len(score) 
    for s in range(len(score)):
        answer[s] = sum(score[s]) / 2

    # 75, 75, 40, 95, 95, 100, 20
    # 75 70 55 65
    answer_list = sorted(answer, reverse=True)
    ans_list = []
    for a in answer:
        ans_list.append(answer_list.index(a) + 1)
    return ans_list


