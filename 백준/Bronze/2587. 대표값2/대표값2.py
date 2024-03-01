num = []
for i in range(1, 6):
  num.append(int(input()))
  num.sort()

print(sum(num)//5)
print(num[2])