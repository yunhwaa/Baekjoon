def solution(answers):
    answer = []
    answer_list = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    n1, n2, n3 = 0, 0, 0
    for i, a in enumerate(answers):
        if a1[i % len(a1)] == a:
            n1 += 1
        if a2[i % len(a2)] == a:
            n2 += 1
        if a3[i % len(a3)] == a:
            n3 += 1
    
    answer_list.append(n1)
    answer_list.append(n2)
    answer_list.append(n3)
    
    max_num = max(answer_list)
    for a in range(len(answer_list)):
        if max_num == answer_list[a]:
            answer.append(a+1)
    
            
    return answer