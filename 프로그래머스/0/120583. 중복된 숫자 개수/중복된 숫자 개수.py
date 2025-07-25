def solution(array, n):
    answer = 0
    for a in array:
        if n == a:
            answer += 1
    return answer