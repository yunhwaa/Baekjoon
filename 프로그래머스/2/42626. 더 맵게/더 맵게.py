import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)  # 리스트를 heap으로 변환

    while len(scoville) >= 2 and scoville[0] < K:
        first_n = heapq.heappop(scoville)
        second_n = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first_n + second_n * 2)
        cnt += 1
    
    # 모든 음식을 다 섞고도 K이상이 안 되는 경우 존재
    # ex) solution([1, 1], 100)  -> 모든 걸 섞어도 100을 못 넘음 -> 1
    return cnt if scoville[0] >= K else -1 
