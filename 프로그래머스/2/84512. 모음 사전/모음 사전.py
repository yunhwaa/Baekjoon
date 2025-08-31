from itertools import combinations_with_replacement

def solution(word):
    word_list = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    answer = 0
    for i, ch in enumerate(word):
        idx = word_list.index(ch)
        answer += idx * weights[i] + 1
    return answer

