def solution(my_string, is_prefix):
    answer = 0
    for i in range(0, len(my_string)):
        if my_string[:i+len(is_prefix)] == is_prefix:
            answer = 1
            break
    return answer