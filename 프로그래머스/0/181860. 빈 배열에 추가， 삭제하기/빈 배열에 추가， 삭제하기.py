def solution(arr, flag):
    answer = []
    for f, a in zip(flag, arr):
        if f == True:
            for i in range(a*2):
                answer.append(a)
        elif f == False:
            answer = answer[:-a]
                
    return answer