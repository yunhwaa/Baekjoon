def solution(s):
    answer = 0
    num_list = s.split(' ')
    for i in range(len(num_list)):
        if num_list[i] == "Z":
            answer -= int(num_list[i-1])
        else:
            answer += int(num_list[i]) 
        
    return answer