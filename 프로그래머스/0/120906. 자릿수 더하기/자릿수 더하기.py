def solution(n):
    answer = 0
    n = str(n)
    for num in n:
        answer += int(num)
    return answer