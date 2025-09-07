import heapq

def solution(jobs):
    answer = 0
    time, end, i = 0, 0, 0
    start = -1
    hq = []
    n = len(jobs)
    
    jobs.sort(key = lambda x: x[0])
    
    while i < n:
        for j in jobs:
            if start < j[0] <= time:
                heapq.heappush(hq, (j[1], j[0]))
        if hq:
            cur = heapq.heappop(hq)
            start = time
            time += cur[0]
            answer += (time - cur[1])
            i += 1
        else:
            time += 1
    return answer // n