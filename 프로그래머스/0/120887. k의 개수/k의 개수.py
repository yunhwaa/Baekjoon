def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        n = str(n)
        for m in range(len(n)):
            if int(n[m]) == k:
                answer += 1
    return answer