N = int(input())

num = [int(N) for N in input().split()]
v = int(input())
count = 0

for i in range(len(num)):
  if num[i] == v:
    count += 1

print(count)