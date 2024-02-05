a, b, c = map(int, input().split())
if (a==b==c):
  price = 10000 + a*1000
  print(price)
elif (a==b or b==c or a==c):
  if a==b or a==c:
    price = 1000 + a*100
    print(price)
  elif b==c:
    price = 1000 + b*100
    print(price)
else:
  price = max(a, b, c)*100
  print(price)