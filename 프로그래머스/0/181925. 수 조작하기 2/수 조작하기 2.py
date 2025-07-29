def solution(numLog):
    answer = ''
    for n in range(len(numLog)-1):
        if numLog[n+1] - numLog[n] == 1:
            answer += 'w'
        elif numLog[n+1] - numLog[n] == -1:
            answer += 's'
        elif numLog[n+1] - numLog[n] == 10:
            answer += 'd'
        elif numLog[n+1] - numLog[n] == -10:
            answer += 'a'
    return answer