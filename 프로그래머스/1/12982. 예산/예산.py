def solution(d, budget):
    d.sort()  
    answer = 0
    
    for cost in d: 
        if budget >= cost:
            budget -= cost
            answer += 1
        else:
            break
    return answer

# 이분탐색
# start, mid, end 이용
# 신청한 총 돈: start + mid + end
# 남는 돈: budget - (start + mid + end)

# 1 2 3 4 5 -> 가장 먼저 d 정렬
# 남는 돈이 더 작을 경우와 클 경우 나눠서 계산
# 