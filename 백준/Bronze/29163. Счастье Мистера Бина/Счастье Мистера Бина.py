N = int(input())
plus, minus = 0, 0
test = [int(N) for N in input().split()]
for i in range(0, len(test)):
  if test[i] % 2 == 0:
    plus += 1
  else:
    minus += 1

if plus > minus:
  print("Happy")
else:
  print("Sad")