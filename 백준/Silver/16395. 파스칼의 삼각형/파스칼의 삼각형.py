n, k = map(int, input().split())
gop1 = 1
gop2 = 1

for i in range(n-k+1, n):
  gop1 *= i

for j in range(1, k):
  gop2 *= j

print(gop1 // gop2)