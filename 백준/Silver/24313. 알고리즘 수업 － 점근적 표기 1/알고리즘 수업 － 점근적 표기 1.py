a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

fn = a1 * n + a0
gn = c * n

if fn <= gn:
  if a1 <= c:
    print(1)
  else:
    print(0)
else:
  print(0)