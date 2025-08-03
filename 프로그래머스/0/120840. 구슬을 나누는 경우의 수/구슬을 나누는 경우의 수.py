def solution(balls, share):
    answer = 0
    # balls: n개
    # share: m개
    a, b, c = 1, 1, 1
    for i  in range(balls, 0, -1):
        a *= i
    
    for j in range(balls-share, 0, -1):
        b *= j
    
    for k in range(share, 0, -1):
        c *= k
        
    answer = a / (b * c)
    return answer