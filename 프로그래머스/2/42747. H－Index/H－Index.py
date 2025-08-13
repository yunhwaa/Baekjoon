def solution(citations):
    answer = 0
    ans_list = []
    
    for c in citations:
        num = c
        count = 0

        for n in citations:
            if n >= c:
                count += 1
                
        if count >= num:
            ans_list.append(num)
        else:
            ans_list.append(count)
    answer = max(ans_list)
    return answer

