n = int(input())
x = 5
count = 0

num = [int(x) for x in input().split()]

for i in range(len(num)):
  if n == num[i]:
    count += 1

print(count)