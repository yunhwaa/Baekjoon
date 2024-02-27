T = int(input())
count = 0

for i in range(1, T+1):
  N, M = map(str, input().split())
  for j in range(int(N), int(M)+1):
    num = str(j)
    for p in range(len(num)):
      if num[p] == '0':
        count += 1
  print(count)
  count = 0