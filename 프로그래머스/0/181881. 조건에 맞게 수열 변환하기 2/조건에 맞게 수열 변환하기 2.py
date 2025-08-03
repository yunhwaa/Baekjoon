def solution(arr):
    answer = 0
    ar1 = arr
    ar2 = []
    
    while ar1 != ar2:
        for a in ar1:
            if a >= 50 and a % 2 == 0:
                ar2.append(a // 2)
            elif a < 50 and a % 2 == 1:
                ar2.append(a * 2 + 1)
        
        if ar1 == ar2:
            break
        else:
            ar1 = ar2
            ar2 = []
            answer += 1
    return answer - 1