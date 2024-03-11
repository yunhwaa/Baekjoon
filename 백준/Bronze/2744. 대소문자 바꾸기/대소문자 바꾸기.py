sentence = input()

for i in range(len(sentence)):
  if sentence[i].islower():
    print(sentence[i].upper(), end="")
  else:
    print(sentence[i].lower(), end="")