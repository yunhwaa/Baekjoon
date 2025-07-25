def solution(array):
    answer = []
    answer.append(max(array))
    for a in range(len(array)):
        if answer[0] == array[a]:
            answer.append(a)
    return answer