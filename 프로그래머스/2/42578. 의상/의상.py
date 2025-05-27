def solution(clothes):
    answer = 1
    closet = {}
    
    for i in clothes:
        category = i[1]
        if category in closet:
            closet[category] += 1
        else:
            closet[category] = 1
    
    for n in closet.values():
        answer *= (n + 1)  # 안 입는 경우도 고려!

    
    return answer - 1    # 모두 안 입는 경우 제외