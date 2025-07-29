def solution(n):
    answer = []
    for i in range(n):
        a = [0] * (n)
        a[i] = 1
        answer.append(a)
    return answer