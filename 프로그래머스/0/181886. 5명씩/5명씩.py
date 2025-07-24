def solution(names):
    answer = []
    for n in range(len(names)):
        if (n+1) % 5 == 1:
            answer.append(names[n])
    return answer