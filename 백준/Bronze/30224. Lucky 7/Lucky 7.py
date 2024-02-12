N = input()
if '7' in N:
  if int(N) % 7 != 0:
    print(2)
  else:
    print(3)
else:
  if int(N) % 7 != 0:
    print(0)
  else:
    print(1)