sentence = input()

for i in range(len(sentence), 0, -1):
  print(sentence[i-1], end="")
