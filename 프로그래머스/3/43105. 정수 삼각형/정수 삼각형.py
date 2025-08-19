def solution(triangle):
    answer = 0
    # bottom-up 방식으로 아래서부터 위로 최댓값 더해서 업데이트 
    # 30 
    # 7
    # 23 21 
    # 20 13 10 
    # 7 12 10 10 
    for tr in range(len(triangle)-1, 0, -1):
        tri = triangle[tr]
        for t in range(len(tri)-1):
            triangle[tr-1][t] += max(tri[t], tri[t+1])
            
    answer = triangle[0][0]
    return answer