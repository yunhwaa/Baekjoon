def solution(n, lost, reserve):
    answer = 0
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    overlap = lost_set & reserve_set
    lost_set -= overlap
    reserve_set -= overlap
    
    for r in sorted(reserve_set):
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
    answer = n - len(lost_set)
    return answer