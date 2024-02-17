import sys

A, B = map(str, sys.stdin.readline().split())
hap = 0

for i in range(0, len(A)):
  for j in range(0, len(B)):
    gop = int(A[i]) * int(B[j])
    hap += gop

print(hap)