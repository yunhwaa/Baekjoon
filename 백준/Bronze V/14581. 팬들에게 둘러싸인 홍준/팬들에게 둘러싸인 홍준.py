id = input()

for i in range(1, 4):
  for j in range(1, 4):
      if i == 2 and j == 2:
        print(":{}:".format(id), end = '')
      else:
        print(":fan:", end = '')
  print("\n".strip())