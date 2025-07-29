def solution(num_str):
    answer = 0
    for n in str(num_str):
        answer += int(n)
    return answer