while True:
  word = input()
  re_word = word[-1:-len(word)-1:-1]

  if word == '0':
    break
  
  if word == re_word:
    print('yes')
  else:
    print('no')