def solution(prices):
    ans = []
    
    for i in range(len(prices)):
        cnt = 0
        j = i + 1
        
        while True:
            if j == len(prices):
                ans.append(cnt) 
                break
            elif prices[j] >= prices[i]:
                cnt += 1
                j += 1
            else:
                cnt += 1
                ans.append(cnt)
                break
        
    return ans
            
        
# i랑 j가 순환
# 1꺼냄 -> prices 길이만큼 비교 -> 중간에 더 작은 수가 나오면 break -> 그렇지 않으면 cnt 1씩 증가 

# i는 prices길이보다 1작은 곳까지 or i가 prices 길이 값이면 0 추가 
# 넣고나면 cnt 다시 0으로 초가 

