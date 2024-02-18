odd = []

for i in range(1, 8):
  num = int(input())
  if num % 2 == 1:
    odd.append(num)

if len(odd) >= 1:
  print(sum(odd))
  min = odd[0]
  for j in range(1, len(odd)):
    if min >= odd[j]:
      min = odd[j]
  print(min)
else:
  print(-1)