def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]*numbers[j])
    answer = sorted(answer)
    return answer[-1]