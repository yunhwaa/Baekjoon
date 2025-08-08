def solution(arr):
    answer = []
    answer.append(arr[0])
    be_ans = arr[0]
    for a in range(1, len(arr)):
        if arr[a] != be_ans:
            answer.append(arr[a])
            be_ans = arr[a]
    return answer