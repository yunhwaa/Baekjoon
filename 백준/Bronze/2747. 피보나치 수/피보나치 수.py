n = int(input())

#작은 문제부터 해결해서 저장할 dp 테이블
dp = [0] * 46

dp[0] = 0
dp[1] = 1
dp[2] = 1

#피보나치 수열을 반복문으로 구현(bottom up)
for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])