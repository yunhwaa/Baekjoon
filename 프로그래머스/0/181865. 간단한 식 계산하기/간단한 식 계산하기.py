def solution(binomial):
    answer = 0
    num_list = binomial.split(' ')
    if num_list[1] == "+":
        answer = int(num_list[0]) + int(num_list[2])
    elif num_list[1] == "-":
        answer = int(num_list[0]) - int(num_list[2])
    elif num_list[1] == "*":
        answer = int(num_list[0]) * int(num_list[2])
    return answer