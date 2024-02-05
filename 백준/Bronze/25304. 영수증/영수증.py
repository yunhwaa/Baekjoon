X = int(input())
N = int(input())
i = 1
hap = 0

while i < N+1:
  a, b = map(int, input().split())
  hap += a*b
  i += 1

if hap == X:
  print("Yes")
else:
  print("No")