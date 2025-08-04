def solution(my_string):
    answer = 0
    st = ''
    for s in my_string:
        if s.isdigit() == True:
            st += str(s)
        elif s.isdigit() == False:
            if len(st) > 0:
                st = int(st)
                answer += st 
                st = ''
    if st:
        answer += int(st)
    
    return answer