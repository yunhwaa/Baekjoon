def solution(array, n):
    answer = array[0]
    num = abs(array[0] - n)
    for a in range(1, len(array)):
        if abs(array[a]-n) < num:
            num = abs(array[a] - n)
            answer = array[a]
        elif abs(array[a] - n) == num:
            answer = min(answer, array[a])
    return answer