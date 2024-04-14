sentence = list(input())
num1, num2 = 0, 0

for i in range(0, len(sentence)):
  if sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u":
    num1 += 1 

for i in range(0, len(sentence)):
  if sentence[i] == "a" or sentence[i] == "e" or sentence[i] == "i" or sentence[i] == "o" or sentence[i] == "u" or sentence[i] == "y":
    num2 += 1 

print("{} {}".format(num1, num2))