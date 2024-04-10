chick_stock = int(input())
coke, beer = map(int, input().split())

drink = coke // 2 + beer

if drink > chick_stock:
  print(chick_stock)
else:
  print(drink)