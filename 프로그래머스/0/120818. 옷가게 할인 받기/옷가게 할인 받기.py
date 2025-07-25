import math 

def solution(price):
    answer = 0
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price
    answer = math.floor(answer)
    return answer