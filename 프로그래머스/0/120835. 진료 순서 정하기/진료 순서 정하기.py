def solution(emergency):
    answer = [0] * len(emergency)
    em = emergency
    em = sorted(em, reverse=True)
    for i in range(len(em)):
        for e in range(len(emergency)):
            if em[i] == emergency[e]:
                answer[e] = i + 1
    return answer