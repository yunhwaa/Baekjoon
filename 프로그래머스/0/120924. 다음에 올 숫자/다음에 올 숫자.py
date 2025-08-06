def solution(common):
    answer = 0
    ans1 = []
    ans2 = []
    for c in range(len(common)-1):
        ans1.append(common[c+1] - common[c])
        if common[c] == 0:
            break
        else:
            ans2.append(common[c+1] / common[c])
    if len(set(ans1)) == 1:
        answer = common[-1] + ans1[-1]
    else:
        answer = common[-1] * ans2[-1]
    return answer