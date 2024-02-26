N = int(input())
num = [int(N) for N in input().split()]
prime_count = 0

for i in range(0, len(num)):
  count = 0
  for j in range(1, num[i]):
    if num[i] % j == 0:
      count += 1
  if count == 1:
    prime_count += 1

print(prime_count)