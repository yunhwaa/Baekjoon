def solution(N, number):
    answer = 0
    # N == number일 경우
    # N을 i번 사용해서 만들 수 있는 수들
    # i번째 경우의 수를 만들 때, 이전 dp[j]와 dp[i-j]를 조합해서 만들 수 있는 수 
    if N == number:
        answer = 1
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
        
        if number in dp[i]:
            return i
    return -1
    

    
    
    return answer