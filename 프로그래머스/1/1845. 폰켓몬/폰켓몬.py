def solution(nums):
    answer = 0
    n = len(nums) // 2
    answer = min(len(set(nums)), n)
    return answer