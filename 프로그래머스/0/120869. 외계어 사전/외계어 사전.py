def solution(spell, dic):
    answer = 2
    for d in dic:
        count = 0
        for s in spell:
            if s in d:
                count += 1
        if len(spell) == count:
            answer = 1
    return answer