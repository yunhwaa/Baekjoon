while True:
  pw = input()
  if pw == "END":
    break

  pw = list(pw)
  for i in range(1, len(pw)+1):
    print(pw[-i], end = "")
  print("")