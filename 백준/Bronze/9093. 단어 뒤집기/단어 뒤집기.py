T = int(input())
re_sentence = []

for i in range(1, T+1):
  sentence = list(input().split())

  for p in range(0, len(sentence)):
    word = sentence[p]
    re_word = word[-1:-len(word)-1:-1]
    re_sentence.append(re_word)
  print(' '.join(re_sentence))
  re_sentence = []