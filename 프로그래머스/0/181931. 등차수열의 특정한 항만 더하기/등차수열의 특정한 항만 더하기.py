def solution(a, d, included):
    answer = 0
    # 등차 수열: dn - (d-a)
    for i in range(len(included)):
        if included[i] == True:
            answer += d * (i+1) - (d - a)
    return answer