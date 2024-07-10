# 2750_수 정렬하기
n = int(input())
a = []

for i in range(1, n+1):
  num = int(input())
  a.append(num)

a.sort()

for num in a:
  print(num)