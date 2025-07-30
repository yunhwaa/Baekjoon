def solution(num_list):
    answer = 0
    sum1 = sum(num_list[::2])
    sum2 = sum(num_list[1::2])
    answer = max(sum1, sum2)
    return answer