from itertools import combinations

def solution(nums):
    # ans = []
    # n = list(combinations(nums, len(nums)//2))
    # ans.append(nunique(n))
    # return max(ans)
    
    return min(len(set(nums)), len(nums)//2)



