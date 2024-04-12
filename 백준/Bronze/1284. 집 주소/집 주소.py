while True:
  num = input()
  wide = len(num) + 1

  if num == '0':
    break


  for i in range(0, len(num)):
    if num[i] == '1':
      wide += 2
    elif num[i] == '0':
      wide += 4
    else:
      wide += 3

  print(wide)