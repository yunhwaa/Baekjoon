def solution(my_string):
    answer = []
    final_ans = ''
    for s in my_string:
        answer.append(s.lower())
    answer = sorted(answer)
    for a in answer:
        final_ans += a
    return final_ans