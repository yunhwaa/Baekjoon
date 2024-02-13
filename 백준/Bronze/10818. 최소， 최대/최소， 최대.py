N = int(input())
arr = list(map(int, input().split()))

min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
  if arr[i] <= min:
    min = arr[i]

for j in range(1, len(arr)):
  if arr[j] >= max:
    max = arr[j]

print("{} {}".format(min, max))