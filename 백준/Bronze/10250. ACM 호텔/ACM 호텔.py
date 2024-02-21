T = int(input())
for i in range(T):
  H, W, N = map(int, input().split())
  if N > H:
    if N % H == 0:
      Height = H
      number = N // H
    else:
      Height = N % H
      number = N // H + 1
  elif N == H:
    Height = H
    number = 1
  else:
    Height = N
    number = 1

  
  room = Height * 100 + number
  print(room)