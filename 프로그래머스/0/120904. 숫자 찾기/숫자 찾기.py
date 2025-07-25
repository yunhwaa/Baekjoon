def solution(num, k):
    answer = -1
    num = str(num)
    for n in range(len(num)):
        if int(num[n]) == k:
            answer = n + 1
            break
    return answer