def solution(arr):
    numbers = []
    operators = []
    for i in range(len(arr)):
        if i % 2 == 0:
            numbers.append(int(arr[i]))
        else:
            operators.append(arr[i])
    # 메모리 (이미 계산한 것 저장)
    memory = {}
    # 재귀함수로 문제 해결 
    def calculate(start_idx, end_idx):
        if start_idx == end_idx:
            num = numbers[start_idx]
            return num, num  # (최댓값, 최솟값)
        
        # 이미 계산했으면 저장된 값 사용
        key = (start_idx, end_idx)
        if key in memory:
            return memory[key]
        
        # 가능한 최댓값과 최솟값 초기화
        max_result = float('-inf')
        min_result = float('inf')
        
        for split_point in range(start_idx, end_idx):
            left_max, left_min = calculate(start_idx, split_point)
            right_max, right_min = calculate(split_point+1, end_idx)
            
            operator = operators[split_point]
            
            possible_results = []
            if operator == '+':
                possible_results = [
                    left_max + right_max,
                    left_max + right_min,
                    left_min + right_max,
                    left_min + right_min
                ]
            else:
                possible_results = [
                    left_max - right_max,
                    left_max - right_min,
                    left_min - right_max,
                    left_min - right_min
                ]
                
            max_result = max(max_result, max(possible_results))
            min_result = min(min_result, min(possible_results))
            
        memory[key] = (max_result, min_result)
        return max_result, min_result
    
    final_max, final_min = calculate(0, len(numbers) - 1)
    return final_max
        
    return answer