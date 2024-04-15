N = int(input())
nocute, cute = 0, 0

for i in range(0, N):
  n = int(input())

  if n == 0:
    nocute += 1
  elif n == 1:
    cute += 1

if nocute > cute:
  print("Junhee is not cute!")
else:
  print("Junhee is cute!")