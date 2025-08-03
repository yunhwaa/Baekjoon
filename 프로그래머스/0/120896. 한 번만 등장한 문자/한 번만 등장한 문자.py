def solution(s):
    answer = ''
    ans = []
    s_set = list(set(s))
    for i in range(len(s_set)):
        if s.count(s_set[i]) == 1:
            ans.append(s_set[i])
    
    ans = sorted(ans)
    for a in ans:
        answer += a
    return answer