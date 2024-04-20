N = 4
start, end = map(int, input().split())
num = end
max = num

for i in range(1, N):
  start, end = map(int, input().split())
  num = num - start + end
  if num > max:
    max = num

print(max)