while True:
  n = int(input())
  hap = 0

  if n == 0:
    break
    
  for i in range(n, 0, -1):
    hap += i
  print(hap)