from itertools import permutations 

def solution(k, dungeons):
    max_count = 0
    
    for perm in permutations(range(len(dungeons))):
        current_k = k
        count = 0
        
        for i in perm:
            if current_k >= dungeons[i][0]:
                current_k -= dungeons[i][1]
                count += 1
            else:
                break
        max_count = max(max_count, count)
    return max_count