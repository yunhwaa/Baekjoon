N, A, B = map(int, input().split())

Bus = A
Subway = N + (B-N)

if Bus < Subway:
  print("Bus")
elif Bus > Subway:
  print("Subway")
else:
  print("Anything") 