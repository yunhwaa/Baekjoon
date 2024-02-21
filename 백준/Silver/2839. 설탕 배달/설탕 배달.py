N = int(input())
sum = []

for i in range(0, N+1):
  for j in range(0, N+1):
    if 3*i + 5*j == N:
      sum.append(i+j)

if len(sum) == 0:
  print(-1)
else:
  print(min(sum))