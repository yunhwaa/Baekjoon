def solution(numbers, direction):
    answer = []
    if direction == "left":
        for n in range(1, len(numbers)+1):
            answer.append(numbers[n % len(numbers)])
    else:
        for n in range(len(numbers)-1, len(numbers)*2-1):
            answer.append(numbers[n % len(numbers)])        
    return answer