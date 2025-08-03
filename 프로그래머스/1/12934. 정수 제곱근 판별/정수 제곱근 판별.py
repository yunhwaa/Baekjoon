def solution(n):
    answer = -1
    for i in range(1, n+1):
        if n / i == i:
            answer = (i+1) * (i+1)
            break
    return answer