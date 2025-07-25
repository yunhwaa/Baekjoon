def solution(num_list):
    answer = []
    n1, n2 = 0, 0
    for n in num_list:
        if n % 2 == 0:
            n1 += 1
        else:
            n2 += 1
    answer.append(n1)
    answer.append(n2)
    return answer