N = input()
name = []

M = N.split('-')

for i in range(0, len(M)):
  word = M[i]
  name.append(word[0])

print("".join(name))