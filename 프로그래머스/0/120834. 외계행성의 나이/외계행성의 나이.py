def solution(age):
    answer = ''
    ans_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    age = str(age)
    for i in range(len(age)):
        answer += ans_list[int(age[i])]

    return answer