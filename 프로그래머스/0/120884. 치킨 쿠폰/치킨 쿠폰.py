def solution(chicken):
    answer = 0
    left = 0
    while chicken + left >= 10:
        total = chicken + left
        chicken = total // 10 
        answer += chicken 
        left = total % 10 
    
    return answer