def solution(s1, s2):
    answer = 0
    for n1 in s1:
        for n2 in s2:
            if n1 == n2:
                answer += 1
    return answer