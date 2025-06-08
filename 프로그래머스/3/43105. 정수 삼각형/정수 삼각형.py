def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
        
        ans = max(triangle[-1])
                
    return ans

# 7
# 3 8 
# 8 1 0
# 아래로 한 칸(+1, 0) / 대각선 오른쪽(+1, +1)
# 맨 아래줄부터 위로 올라가며 각 숫자에 대해 아래 칸 두 개 중 더 큰 값을 더해줌

