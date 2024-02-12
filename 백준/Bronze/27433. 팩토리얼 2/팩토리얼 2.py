N = int(input())
fac = 1

if N == 0:
  fac = 1
else:
  for i in range(N, 0, -1):
    fac *= i

print(fac)