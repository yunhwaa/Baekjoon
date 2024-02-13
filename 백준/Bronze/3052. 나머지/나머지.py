a = []
b = []
count = 0

for i in range(1, 11):
  num = int(input())
  a.append(num % 42)

for j in range(0, len(a)):
  if a[j] not in b:
    b.append(a[j])
    count += 1

print(count)