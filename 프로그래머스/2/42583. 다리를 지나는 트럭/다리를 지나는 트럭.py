def solution(bridge_length, weight, truck_weights):
    time = 0
    passing_truck = [0] * bridge_length # 다리 건너는 트럭
    sum_weight = 0
    
    while len(truck_weights) > 0:
        time += 1
        sum_weight -= passing_truck.pop(0)
        
        if sum_weight + truck_weights[0] <= weight:
            sum_weight += truck_weights[0]
            passing_truck.append(truck_weights.pop(0))
        else:
            passing_truck.append(0)
    
    time += bridge_length
    return time
# 대기 트럭에서 맨 앞에꺼 빼서 다리 건너는 트럭(passing_truck)에 넣어
# 다리 건너는 트럭이 bridge_length대보다 작고, weight보다 작으면 
# time에 bridge 개수만큼 더하기 
# 다리를 지난 트럭이 대기 트럭에 있는 수와 똑같으면 time 리턴 

# bridge_length: 다리에 올라갈 수 있는 트럭 개수(최대 트럭 수)
# weight: 한 다리에 올라갈 수 있는 무게
# truck_weights: 트럭 별 무게 
