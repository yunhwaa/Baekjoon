count = 0

for i in range(1, 9):
  state = input()

  if i % 2 != 0:
    for j in range(0, 7, 2):
      if state[j] == 'F':
        count += 1
  
  else:
    for j in range(1, 8, 2):
      if state[j] == 'F':
        count += 1

print(count)