while True:
  x, y, z = map(int, input().split())

  if x == 0 and y == 0 and z == 0:
    break

  if x>=y and x>=z:
    if y*y + z*z == x*x:
      print("right")
    else:
      print("wrong")
  elif y>=x and y>=z:
    if x*x + z*z == y*y:
      print("right")
    else:
      print("wrong")
  else:
    if x*x + y*y == z*z:
      print("right")
    else:
      print("wrong") 