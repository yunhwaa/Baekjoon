def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for num in num_list:
        if num % 2 == 1:
            odd += str(num)
        else:
            even += str(num)
    answer = int(odd) + int(even)
    return answer