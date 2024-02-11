N = int(input())

for i in range(1, N+1):
  A, B, X = map(int, input().split())
  print(A*(X-1) + B) 