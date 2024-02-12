N = int(input())

if N == 0:
  fac = 1
else:
  fac = 1
  for i in range(N, 1, -1):
    fac *= i

print(fac)