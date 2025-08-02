def solution(arr):
    answer = []
    ans = [] 
    if arr.count(2) == 0:
        answer.append(-1)
    elif arr.count(2) == 1:
        answer.append(2)
    else:
        for i in range(len(arr)):
            if arr[i] == 2:
                ans.append(i)
        answer = arr[ans[0]:ans[-1]+1]
    return answer