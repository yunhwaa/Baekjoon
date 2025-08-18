import heapq 

def solution(operations):
    heap = []
    answer = []
    for num in operations:
        n, m = num.split(' ')
        m = int(m)
        
        if n == "I":
            heapq.heappush(heap, m)
        elif n == "D":
            if not heap:
                continue
            if m == 1:
                heap = sorted(heap)
                heap.remove(heap[-1])
            elif m == -1:
                heapq.heappop(heap)
                
    if len(heap) == 0:
        answer.append(0)
        answer.append(0)
    else:
        heap = sorted(heap)
        answer.append(heap[-1])
        answer.append(heap[0])
    
    
    return answer