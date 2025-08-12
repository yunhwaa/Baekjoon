from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    t_weight = 0
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    
    while truck or t_weight > 0:
        time += 1
        t = bridge.popleft()
        t_weight -= t
        
        if truck and t_weight + truck[0] <= weight:
            t = truck.popleft()
            bridge.append(t)
            t_weight += t
        else:
            bridge.append(0)       
    return time

