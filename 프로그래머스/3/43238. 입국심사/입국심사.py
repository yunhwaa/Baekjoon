def solution(n, times):
    left = 1
    right = max(times) * n  # 최악의 경우 
    answer = right  
    
    while left <= right:
        mid = (left + right) // 2
        total = sum(mid // t for t in times)
        
        if total >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

# 2명은 바로 출발
# 7분 -> 3
# 10분 -> 4
# 14분 -> 5
# 20분 -> 6
# 21분 -> 7
# 25분 -> 8

# 최대 시간: max(times) * n
# 가장 느린 심사대가 n명 심사할 때 걸리는 시간 -> 가장 최악의 경우 

