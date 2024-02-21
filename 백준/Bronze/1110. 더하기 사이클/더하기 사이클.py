N = int(input())
num = N
cycle = 0

while True:
  a = N // 10 + N % 10
  b = int(str(N % 10) + str(a % 10))
  N = b

  cycle += 1

  if N == num:
    print(cycle)
    break