def solution(N, number):
    if N == number:
        return 1

    # 각 i개의 N으로 만들 수 있는 수들의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].update({x+y, x-y, x*y})
                    
                    if y != 0:
                        dp[i].add(x//y)
        
        if number in dp[i]:
            return i
    return -1