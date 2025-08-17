import heapq 
heapq.heapify
def solution(scoville, K):
    
    answer = 0
    heapq.heapify(scoville)
    while True:
        
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            return -1 
            
        num1, num2 = heapq.heappop(scoville), heapq.heappop(scoville)
        num = num1 + (num2 * 2) 
        heapq.heappush(scoville, num)
        answer += 1
        
    return answer