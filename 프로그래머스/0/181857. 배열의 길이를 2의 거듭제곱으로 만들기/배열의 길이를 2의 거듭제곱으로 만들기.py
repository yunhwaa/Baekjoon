def solution(arr):
    answer = []
    num = 1 
    while len(arr) > num:
        num *= 2
    
    for i in range(num - len(arr)):
        arr.append(0)
    return arr