N = 8
num = [int(N) for N in input().split()]
asc, desc, mix = 0, 0, 0

for i in range(1, 9):
  if i == num[i-1]:
    asc += 1
  elif i == num[-i]:
    desc += 1
  else:
    mix += 1

if asc == 8:
  print("ascending")
elif desc == 8:
  print("descending")
else:
  print("mixed")