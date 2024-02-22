N, K = map(int, input().split())
upper = 1
under = 1

for i in range(N, N-K, -1):
  upper *= i

for j in range(1, K+1):
  under *= j

print(upper//under)