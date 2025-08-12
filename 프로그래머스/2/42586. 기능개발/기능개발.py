def solution(progresses, speeds):
    answer = []
    # [7, 3, 9]
    # [5, 10, 1, 1, 20, 1] -> [1, 3, 2]
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            progresses[i] = (100 - progresses[i]) // speeds[i] + 1
        else:
            progresses[i] = (100 - progresses[i]) // speeds[i]
    count = 0
    
    # 자신보다 큰 수를 만나기 전까지 count를 1씩 증가 시키고 
    # 큰 수 만나면 answer에 count 집어넣기 
    ans_list = []
    ans_list.append(progresses[0])
    for p in range(1, len(progresses)):
        if progresses[p] > ans_list[0]: 
            answer.append(len(ans_list))
            ans_list = [progresses[p]]
        else:
            ans_list.append(progresses[p])
    
    if ans_list:
        answer.append(len(ans_list))

    return answer