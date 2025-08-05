import math 
def solution(a, b):
    answer = 0
    gcd = math.gcd(a, b)
    b //= gcd
    
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    
    if b == 1:
        answer = 1
    else:
        answer = 2
    return answer