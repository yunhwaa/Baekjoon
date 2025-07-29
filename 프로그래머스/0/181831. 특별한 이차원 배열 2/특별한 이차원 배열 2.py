def solution(arr):
    answer = 0
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer = 1
            elif arr[i][j] != arr[j][i]:
                answer = 0
                count += 1
    
    if count > 0:
        answer = 0
        
    return answer