T = int(input())
answer = [int(N) for N in input().split()]
count = 0

for i in range(0, len(answer)):
  if T == answer[i]:
    count += 1

print(count)