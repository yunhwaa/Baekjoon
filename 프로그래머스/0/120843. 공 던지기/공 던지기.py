def solution(numbers, k):
    answer = 0
    for i in range(k-1):
        answer = (answer + 2) % len(numbers)
    answer = numbers[answer]
    return answer