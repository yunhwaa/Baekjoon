a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())

apple = a1 * 3 + a2 * 2 + a3
banana = b1 * 3 + b2 * 2 + b3

if apple > banana:
  print("A")
elif apple < banana:
  print("B")
else:
  print("T")