n = int(input())
for i in range(0, n):
  a, b, c = map(float, input().split())
  hap = a*b*c
  print(f'${hap:.02f}')