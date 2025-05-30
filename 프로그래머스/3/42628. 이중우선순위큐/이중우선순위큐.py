import heapq

def solution(operations):
    heap = []
    
    for num in operations:
        n, m = num.split(" ")
        m = int(m)
        
        if n == "I":
            heapq.heappush(heap, m)  # 작은 수 맨 앞에 
            
        elif n == "D":
            if not heap:
                continue
                
            if m == 1:
                heap = sorted(heap)
                heap.pop()
                heapq.heapify(heap)
                
            elif m == -1:
                heapq.heappop(heap)
    
          
            
    if len(heap) == 0:
        heap = [0, 0]
    else:
        heap = sorted(heap)
        return (heap[-1], heap[0])
        
    return heap