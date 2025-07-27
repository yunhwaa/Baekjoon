def solution(num, total):
    answer = []
    if num % 2 == 1:
        n = total // num - num // 2
    else:
        n = total // num - num // 2 + 1
    
    for i in range(num):
        answer.append(n+i)
    return answer