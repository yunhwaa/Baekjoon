N = int(input())

if N == 1:
  print(" " * (N-1) + "*")
else:
  for i in range(1, N+1):
    print(" " * (N-i) + "* " * i)