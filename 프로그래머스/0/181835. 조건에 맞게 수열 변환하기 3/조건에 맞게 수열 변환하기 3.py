def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for a in arr:
            a *= k
            answer.append(a)
    else:
        for a in arr:
            a += k
            answer.append(a)
            
    return answer