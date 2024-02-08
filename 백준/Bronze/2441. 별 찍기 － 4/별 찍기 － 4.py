N = int(input())

for i in range(1, N+1):
  print(" " * (i-1) + "*" * (-i+(N+1)))