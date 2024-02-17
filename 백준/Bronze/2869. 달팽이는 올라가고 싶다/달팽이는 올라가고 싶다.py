A, B, V = map(int, input().split())
height = V - A
day = height % (A-B)


if day == 0:
  print(height // (A-B) + 1)
else:
  print(height // (A-B) + 2)