while True:
  test = int(input())
  if test == 0:
    break
  elif test % 42 == 0:
    print("PREMIADO")
  else:
    print("TENTE NOVAMENTE")