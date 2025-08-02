def solution(strArr):
    answer = 0
    a = [0] * len(strArr)
    for s in strArr:
        a[len(s)] += 1
    answer = max(a)
    return answer