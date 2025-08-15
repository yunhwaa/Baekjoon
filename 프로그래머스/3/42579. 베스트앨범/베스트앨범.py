def solution(genres, plays):
    answer = []
    gen_dict = {}
    for g, p in zip(genres, plays):
        if g not in gen_dict.keys():
            gen_dict[g] = p
        else:
            gen_dict[g] += p
            
    gen_dict = sorted(gen_dict.items(), key = lambda item: item[1], reverse=True)     
    
    for k, y in gen_dict:
        ans_list = []
        for i, (g, p) in enumerate(zip(genres, plays)):
            if k == g:
                ans_list.append([p, i])
        ans_list = sorted(ans_list, key = lambda x: [-x[0], x[1]])
        answer.append(ans_list[0][1])
        if len(ans_list) > 1:
            answer.append(ans_list[1][1])

    return answer