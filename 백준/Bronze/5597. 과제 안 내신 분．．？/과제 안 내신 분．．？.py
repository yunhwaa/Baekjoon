num = []
left_num = []
for i in range(1, 29):
  num.append(int(input()))
for j in range(1, 31):
  if j not in num:
    left_num.append(j)

left_num.sort()
for p in range(len(left_num)):
  print(left_num[p])