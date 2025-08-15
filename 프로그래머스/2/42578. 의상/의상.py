def solution(clothes):
    answer = 1
    clo_dict = {}
    for c in clothes:
        if c[1] not in clo_dict.keys():
            clo_dict[c[1]] = 1
        else:
            clo_dict[c[1]] += 1
    num = list(clo_dict.values())
    for n in num:
        answer *= (n+1) 
    answer -= 1
    return answer