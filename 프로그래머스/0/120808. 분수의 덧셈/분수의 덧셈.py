import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    a, b = 0, 0  # 분모, 분자 
    a = numer1 * denom2 + numer2 * denom1 
    b = denom1 * denom2
    
    n = math.gcd(a, b)
    a = a // n
    b = b // n
    answer.append(a)
    answer.append(b)
    return answer