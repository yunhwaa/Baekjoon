def solution(intStrs, k, s, l):
    answer = []
    ans_list = []
    for i in intStrs:
        ans_list.append(int(i[s:s+l]))
    for a in ans_list:
        if a > k:
            answer.append(a)
    return answer