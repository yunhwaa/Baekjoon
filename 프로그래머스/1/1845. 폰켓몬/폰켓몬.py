def solution(nums):
    hash_set = set()  # 고유 포켓몬 종류 저장
    
    for num in nums:
        hash_set.add(num)  # 중복 없이 저장됨
        
    select_count = len(nums) // 2  # 고를 수 있는 수: 전체 포켓몬 수의 절반
    return min(len(hash_set), select_count)
    
    # return min(len(set(nums)), len(nums)//2)



