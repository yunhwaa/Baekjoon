def solution(brown, yellow):
    answer = []
    # 내부 면적: w * h
    # 내부 면적: (w-2)*(h-2) = yellow
    num = brown + yellow 
    
    for n in range(num-1, 0, -1):
        if num % n == 0:
            a = n
            b = num // n
            
            if a >= b and (a-2) * (b-2) == yellow:
                answer.append(a)
                answer.append(b)
                break
        else:
            continue
                
    return answer