word = input()
count = 0

for i in range(0, len(word)):
  if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
    count += 1

print(count)