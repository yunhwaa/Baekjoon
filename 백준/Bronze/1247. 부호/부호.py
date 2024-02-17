import sys

for _ in range(3):
  N = int(sys.stdin.readline())
  S = 0

  for i in range(1, N+1):
    num = int(sys.stdin.readline())
    S += num

  if S > 0:
    print("+")
  elif S == 0:
    print(0)
  else:
    print("-") 