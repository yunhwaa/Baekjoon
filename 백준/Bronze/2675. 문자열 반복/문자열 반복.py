T = int(input())

for i in range(1, T+1):
  R, P = input().split()
  for p in range(0, len(P)):
    print(P[p]*int(R), end="")
  print("")