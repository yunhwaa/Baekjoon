A = int(input())
B = int(input())
C = int(input())
result = list(str(A*B*C))

for i in range(0, 10):
  count = 0
  for j in range(len(result)):
    if str(i) == result[j]:
      count += 1
  print(count)