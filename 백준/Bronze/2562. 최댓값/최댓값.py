num = 1
max = int(input())

for i in range(2, 10):
  temp = int(input())
  if temp > max:
    max = temp
    num = i

print(max)
print(num)