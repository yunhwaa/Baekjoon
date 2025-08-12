from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque((p, i) for i, p in enumerate(priorities))
    
    while queue:
        current = queue.popleft()
        
        if queue and current[0] < max(queue)[0]:
            queue.append(current)
        else:
            answer += 1
            if current[1] == location:
                break
            
    return answer