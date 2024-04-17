N = int(input())
num = []

for i in range(0, N):
  test = list(input())
  print(test[0], end="")
  for j in range(1, len(test)):
    if test[j] != test[j-1]:
      print(test[j], end="")
  print("")