T, S = map(int, input().split())

if S == 1 or T > 16 or T <= 11:
  print(280)
elif T >= 12 and T <= 16 and S == 0:
  print(320)