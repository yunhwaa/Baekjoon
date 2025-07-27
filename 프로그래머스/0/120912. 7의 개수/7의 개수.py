def solution(array):
    answer = 0
    for a in array:
        word = str(a)
        for i in range(len(word)):
            if '7' in word[i]:
                answer += 1
    return answer