S = ['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']

N = int(input())
count = 0

for i in range(1, N+1):
  sentence = input()
  if sentence in S:
    count += 1

if count == N:
  print("No")
else:
  print("Yes")