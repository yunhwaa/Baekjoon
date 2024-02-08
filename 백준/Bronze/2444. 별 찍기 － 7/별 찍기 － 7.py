N = int(input())

for p in range(1, N+1):
  print(" "*(N-p) + "*" * (2*p - 1))

for q in range(N-1, 0, -1):
  print(" " * (N-q) + "*" * (2*q - 1))