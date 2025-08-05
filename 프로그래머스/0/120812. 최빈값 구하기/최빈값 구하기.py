def solution(array):
    answer = [0] * (max(array) + 1)
    for a in array:
        answer[a] += 1
    ans = -1
    ans = answer.index(max(answer))

    if answer.count(max(answer)) >= 2:
        ans = -1
    return ans