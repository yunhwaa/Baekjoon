import math
def solution(n):
    answer = 2
    if n % math.sqrt(n) == 0:
        answer = 1
    return answer