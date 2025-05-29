import heapq

def solution(jobs):
    
    jobs.sort()  # 요청 시각 순으로 정렬
    
    total_time = 0 # 총 반환 시간 누적 
    heap = []  # 대기 큐
    time = 0  # 현재 시간
    i = 0  # jobs 인덱스
    count = 0 # 완료 작업 수
    
    while count < len(jobs):  # 작업을 다 처리할 때까지 반복 
        # 현재 시간까지 들어온 모든 작업을 힙에 넣기 (소요 시간 기준)
        while i < len(jobs) and jobs[i][0] <= time:  # jobs[i][0] <= time: 현재 시점까지 요청된 작업
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))  # (소요시간, 요청시각) / 우선순위 기준": 소요 시간이 짧은 게 먼저, 같으면 요청 빠른 게 먼저
            i += 1
            
        if heap:  # 힙에 작업이 하나라도 있으면 
            work_time, start_time = heapq.heappop(heap)  # 가장 소요시간 짧은 작업 꺼냄
            time += work_time  # 디스크가 작업 처리하는 데 소비하는 시간 
            total_time += time - start_time  # 반환 시간 = 현재 시점(time) - 요청 시각(start_time)
            count += 1   # 완료된 작업 수 
        else:
            # 대기 작업이 없으면 다음 작업까지 시간 점프
            time = jobs[i][0]
        
    return total_time // len(jobs)