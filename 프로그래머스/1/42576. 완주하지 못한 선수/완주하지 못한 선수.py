from collections import Counter

def solution(participant, completion):
    answer = ''
    counter = Counter(participant) - Counter(completion)
    answer = list(counter.elements())
    return answer[0]