a = int(input())
b = int(input())
c = int(input())

angle = a + b + c

if angle == 180:
  if a == b == c:
    print("Equilateral")
  elif a == b or b == c or a == c:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")