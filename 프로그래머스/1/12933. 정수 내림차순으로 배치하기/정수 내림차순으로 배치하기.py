def solution(n):
    answer = ''
    n = str(n)
    ans = []
    for i in range(len(n)):
        ans.append(n[i])
    ans = sorted(ans, reverse=True)
    for a in ans:
        answer += a
    answer = int(answer)
    return answer