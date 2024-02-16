T = int(input())

for i in range(1, T+1):
  a, b = map(int, input().split())
  
  num = pow(a, b, 10)

  if num == 0:
    print(10)
  else:
    print(num)