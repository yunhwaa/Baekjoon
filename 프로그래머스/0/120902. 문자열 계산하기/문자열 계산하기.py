def solution(my_string):
    answer = 0
    st = my_string.split(' ')
    answer += int(st[0])
    for s in range(1, len(st), 2):
        if st[s] == "+":
            answer += int(st[s+1])
        elif st[s] == "-":
            answer -= int(st[s+1])
    return answer