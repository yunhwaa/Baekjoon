num = input()
sum = 0

if len(num) == 2:
  for i in range(0, len(num)):
    sum += int(num[i])
elif len(num) == 3:
  if int(num[1]) == 0:
    sum = 10 + int(num[-1])
  else:
    sum = int(num[0]) + 10
elif len(num) == 4:
  sum = 10 + 10

print(sum)