def solution(arr, n):
    answer = []
    if len(arr) % 2 == 1:
        for a in range(0, len(arr), 2):
            arr[a] += n
    elif len(arr) % 2 == 0:
        for a in range(1, len(arr), 2):
            arr[a] += n
    return arr