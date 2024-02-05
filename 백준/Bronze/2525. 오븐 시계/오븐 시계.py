H, M = map(int, input().split())
time = int(input())
if M + time >= 60:
  H = H + (M+time)//60 
  M = (M+time) % 60
  if H >= 24:
    H = H - 24
  print(H, M)
else:
  M = M + time
  print(H, M)